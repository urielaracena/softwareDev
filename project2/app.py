import os
from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date, time, timedelta
import json

# Create Flask app
app = Flask(__name__)

# App configuration
database_url = os.environ.get('DATABASE_URL')
# Handle Render's postgres:// vs postgresql:// issue
if database_url and database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url or 'postgresql://postgres:aracena@localhost/salon_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(24))

# Initialize database
db = SQLAlchemy(app)

# Initialize migration
migrate = Migrate(app, db)

# Initialize login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    bookings = db.relationship('Booking', backref='client', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer)  # duration in minutes
    category = db.Column(db.String(50), nullable=False)  # e.g., 'haircut', 'color', 'spa'
    bookings = db.relationship('Booking', backref='service', lazy=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, completed, canceled
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Login manager user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Helper function to get services by category
def get_services_by_category(category):
    return Service.query.filter_by(category=category).all()

# Context processor for template usage
@app.context_processor
def utility_functions():
    def get_services_by_category(category):
        return Service.query.filter_by(category=category).all()
    
    def get_all_services():
        return Service.query.all()
    
    return dict(
        get_services_by_category=get_services_by_category,
        get_all_services=get_all_services
    )

# Forms
class RegistrationForm:
    def __init__(self):
        self.username = None
        self.email = None
        self.password = None
        self.confirm_password = None
        self.first_name = None
        self.last_name = None
        self.phone = None
        self.errors = {}
        
    def validate_on_submit(self):
        if request.method == 'POST':
            self.username = request.form.get('username')
            self.email = request.form.get('email')
            self.password = request.form.get('password')
            self.confirm_password = request.form.get('confirm_password')
            self.first_name = request.form.get('first_name')
            self.last_name = request.form.get('last_name')
            self.phone = request.form.get('phone')
            
            # Validations
            if not self.username or len(self.username) < 3:
                self.errors['username'] = 'Username must be at least 3 characters'
            
            if not self.email or '@' not in self.email:
                self.errors['email'] = 'Valid email is required'
                
            if User.query.filter_by(username=self.username).first():
                self.errors['username'] = 'Username is already taken'
                
            if User.query.filter_by(email=self.email).first():
                self.errors['email'] = 'Email is already registered'
                
            if not self.password or len(self.password) < 6:
                self.errors['password'] = 'Password must be at least 6 characters'
                
            if self.password != self.confirm_password:
                self.errors['confirm_password'] = 'Passwords must match'
                
            return len(self.errors) == 0
        return False

class LoginForm:
    def __init__(self):
        self.username = None
        self.password = None
        self.errors = {}
        
    def validate_on_submit(self):
        if request.method == 'POST':
            self.username = request.form.get('username')
            self.password = request.form.get('password')
            
            # Validations
            if not self.username:
                self.errors['username'] = 'Username is required'
                
            if not self.password:
                self.errors['password'] = 'Password is required'
                
            return len(self.errors) == 0
        return False

class BookingForm:
    def __init__(self):
        self.service_id = None
        self.date = None
        self.time = None
        self.errors = {}
        
    def validate_on_submit(self):
        if request.method == 'POST':
            self.service_id = request.form.get('service_id')
            self.date = request.form.get('date')
            self.time = request.form.get('time')
            
            # Validations
            if not self.service_id:
                self.errors['service_id'] = 'Service is required'
                
            if not self.date:
                self.errors['date'] = 'Date is required'
                
            if not self.time:
                self.errors['time'] = 'Time is required'
                
            return len(self.errors) == 0
        return False

# Helper function to add sample services
def add_sample_services():
    # Check if services already exist to avoid duplicates
    if Service.query.count() == 0:
        # Add services to the database
        services = [
            # Hair Services
            Service(name="Signature Haircut", description="Custom cut with wash, blow-dry, and styling", price=60.00, duration=60, category="hair"),
            Service(name="Precision Haircut", description="Clean, tailored haircut with finishing style", price=40.00, duration=45, category="hair"),
            Service(name="Balayage Highlights", description="Soft, hand-painted highlights for a natural glow", price=120.00, duration=150, category="hair"),
            Service(name="Color Refresh", description="Touch-up and tone to maintain hair color vibrancy", price=70.00, duration=90, category="hair"),
            Service(name="Hydrating Blowout", description="Moisturizing treatment with blow-dry and style", price=55.00, duration=60, category="hair"),
            
            # Waxing Services
            Service(name="Brow Shaping", description="Custom brow shaping using wax or threading", price=20.00, duration=20, category="waxing"),
            Service(name="Full Face Wax", description="Smooth finish for cheeks, lip, and chin areas", price=40.00, duration=30, category="waxing"),
            Service(name="Bikini Line Wax", description="Clean and neat bikini area waxing", price=50.00, duration=30, category="waxing"),
            
            # Nail Services
            Service(name="Classic Manicure", description="Nail shaping, cuticle care, massage, and polish", price=30.00, duration=40, category="nails"),
            Service(name="Gel Manicure", description="Long-lasting gel polish with UV curing", price=45.00, duration=50, category="nails"),
            Service(name="Spa Pedicure", description="Exfoliation, massage, mask, and polish", price=55.00, duration=60, category="nails"),
            Service(name="Nail Art Add-On", description="Custom nail design available on request", price=15.00, duration=15, category="nails"),

            # Facial Services
            Service(name="Express Glow Facial", description="Quick facial to refresh and hydrate the skin", price=45.00, duration=30, category="facial"),
            Service(name="Anti-Aging Facial", description="Firming and rejuvenating treatment", price=85.00, duration=75, category="facial"),
            Service(name="Deep Hydration Facial", description="Restorative moisture treatment for dry skin", price=95.00, duration=80, category="facial")
        ]
        
        # Add all services to the database
        for service in services:
            db.session.add(service)
        
        # Commit the changes
        db.session.commit()
        
        print(f"Added {len(services)} services to the database")

# Routes
@app.route('/')
def index():
    featured_services = Service.query.limit(3).all()
    # Debug print to see if services exist
    print(f"Found {len(featured_services)} featured services")
    return render_template('index.html', services=featured_services)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def all_services():
    categories = db.session.query(Service.category).distinct().all()
    categories = [category[0] for category in categories]
    # Debug print
    print(f"Found {len(categories)} service categories")
    # Get all services for debugging
    all_services = Service.query.all()
    print(f"Total services in database: {len(all_services)}")
    return render_template('all_services.html', categories=categories)

@app.route('/services/<category>')
def services_by_category(category):
    # Log the requested category for debugging
    print(f"Requested category: {category}")
    
    # Get all services for this category
    services = Service.query.filter_by(category=category).all()
    
    # Debug: print found services
    print(f"Found {len(services)} services in category '{category}'")
    if services:
        for service in services:
            print(f"  - {service.name} (${service.price})")
    
    return render_template('services_by_category.html', services=services, category=category)

@app.route('/debug/services')
def debug_services():
    """Debug endpoint to check all services in the database"""
    all_services = Service.query.all()
    categories = db.session.query(Service.category).distinct().all()
    categories = [cat[0] for cat in categories]
    
    data = {
        'total_services': len(all_services),
        'categories': categories,
        'services_by_category': {}
    }
    
    for category in categories:
        category_services = Service.query.filter_by(category=category).all()
        data['services_by_category'][category] = [
            {
                'id': service.id,
                'name': service.name,
                'price': service.price,
                'duration': service.duration
            }
            for service in category_services
        ]
    
    return jsonify(data)

@app.route('/cart')
def cart():
    if 'cart' not in session:
        session['cart'] = []
    cart_items = session.get('cart', [])
    total_price = sum(item['price'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

# Cart management routes
@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    service_id = request.form.get('service_id')
    
    # Fetch service details from database
    service = Service.query.get(service_id)
    if not service:
        flash('Service not found', 'danger')
        return redirect(request.referrer or url_for('all_services'))
    
    # Initialize cart if not exists
    if 'cart' not in session:
        session['cart'] = []
    
    # Check if service is already in cart
    cart_item_ids = [item['id'] for item in session['cart']]
    if service_id in cart_item_ids:
        flash(f'{service.name} is already selected', 'warning')
        return redirect(request.referrer or url_for('all_services'))
    
    # Add item to cart
    cart_item = {
        'id': service_id,
        'name': service.name,
        'price': float(service.price),
        'duration': service.duration
    }
    session['cart'].append(cart_item)
    session.modified = True
    
    flash(f'{service.name} added to your appointment', 'success')
    return redirect(request.referrer or url_for('all_services'))

@app.route('/remove-from-cart', methods=['POST'])
def remove_from_cart():
    service_id = request.form.get('service_id')
    
    if 'cart' in session:
        # Find and remove the item from cart
        for i, item in enumerate(session['cart']):
            if item['id'] == service_id:
                removed_item = session['cart'].pop(i)
                session.modified = True
                flash(f'{removed_item["name"]} removed from cart', 'success')
                break
    
    return redirect(url_for('checkout'))

@app.route('/clear-cart', methods=['POST'])
def clear_cart():
    if 'cart' in session:
        session.pop('cart')
        flash('Your cart has been cleared', 'success')
    
    return redirect(url_for('checkout'))

@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    cart_items = session.get('cart', [])
    total_price = sum(item['price'] for item in cart_items)
    total_duration = sum(item['duration'] for item in cart_items)
    min_date = datetime.now().strftime('%Y-%m-%d')
    available_times = ["9:00 AM", "10:00 AM", "11:00 AM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM"]

    if request.method == 'POST':
        selected_date = request.form.get('date')
        selected_time = request.form.get('time')
        notes = request.form.get('notes')

        if not selected_date or not selected_time:
            flash('Please select both date and time for your appointment.', 'danger')
            return redirect(url_for('checkout'))

        try:
            booking_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            booking_time = datetime.strptime(selected_time, '%I:%M %p').time()
        except ValueError:
            flash('Invalid date or time format.', 'danger')
            return redirect(url_for('checkout'))

        for item in cart_items:
            new_booking = Booking(
                date=booking_date,
                time=booking_time,
                user_id=current_user.id,
                service_id=int(item['id']),
            )
            db.session.add(new_booking)

        db.session.commit()
        session.pop('cart', None)
        flash('Your appointment has been booked successfully!', 'success')
        return redirect(url_for('dashboard'))

    return render_template(
        'checkout.html',
        cart_items=cart_items,
        total_price=total_price,
        total_duration=total_duration,
        min_date=min_date,
        available_times=available_times
    )


@app.route('/get-available-times')
def get_available_times():
    selected_date = request.args.get('date')
    
    # In a real application, you would:
    # 1. Query your database for existing appointments on this date
    # 2. Consider staff availability, business hours, etc.
    # 3. Calculate available time slots based on the selected services' duration
    
    # For this example, we'll return a static list
    # But you'd customize this based on the selected date
    available_times = ["9:00 AM", "10:00 AM", "11:00 AM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM"]
    
    # You could modify available times based on weekday
    if selected_date:
        date_obj = datetime.strptime(selected_date, '%Y-%m-%d')
        if date_obj.weekday() >= 5:  # Weekend
            available_times = ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM"]
    
    return jsonify({'times': available_times})

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
        
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username,
            email=form.email,
            first_name=form.first_name,
            last_name=form.last_name,
            phone=form.phone
        )
        new_user.set_password(form.password)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created successfully! You can now login.', 'success')
        return redirect(url_for('login'))
        
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
        
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username).first()
        
        if user and user.check_password(form.password):
            login_user(user)
            next_page = request.args.get('next')
            flash('Login successful!', 'success')
            return redirect(next_page or url_for('dashboard'))
        else:
            flash('Login unsuccessful. Please check your username and password.', 'danger')
            
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    user_bookings = Booking.query.filter_by(user_id=current_user.id).order_by(Booking.date, Booking.time).all()
    return render_template('dashboard.html', bookings=user_bookings)

@app.route('/book', methods=['GET', 'POST'])
@login_required
def book_service():
    form = BookingForm()
    services = Service.query.all()
    
    if form.validate_on_submit():
        service = Service.query.get(form.service_id)
        
        if service:
            # Convert date and time strings to Python date and time objects
            date_obj = datetime.strptime(form.date, '%Y-%m-%d').date()
            time_obj = datetime.strptime(form.time, '%H:%M').time()
            
            new_booking = Booking(
                date=date_obj,
                time=time_obj,
                user_id=current_user.id,
                service_id=service.id
            )
            
            db.session.add(new_booking)
            db.session.commit()
            
            flash('Your appointment has been booked successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Service not found.', 'danger')
            
    return render_template('booking.html', form=form, services=services)

@app.route('/booking/<int:booking_id>/cancel')
@login_required
def cancel_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    
    if booking.user_id != current_user.id:
        flash('You are not authorized to cancel this booking.', 'danger')
        return redirect(url_for('dashboard'))
        
    booking.status = 'canceled'
    db.session.commit()
    
    flash('Your appointment has been canceled.', 'info')
    return redirect(url_for('dashboard'))

# Admin dashboard route
@app.route('/admin', methods=['GET'])
@login_required
def admin_dashboard():
    # TODO: Add actual admin check
    # This is a placeholder for demonstration
    if current_user.username != 'admin':
        flash('You do not have permission to access the admin dashboard.', 'danger')
        return redirect(url_for('dashboard'))
    
    # Get all bookings for admin view
    all_bookings = Booking.query.order_by(Booking.date, Booking.time).all()
    all_users = User.query.all()
    all_services = Service.query.all()
    
    return render_template(
        'admin_dashboard.html', 
        bookings=all_bookings,
        users=all_users,
        services=all_services
    )

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Create database tables within application context
with app.app_context():
    db.create_all()
    add_sample_services()

# Port configuration for Render
port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False)