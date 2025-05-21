'''
Uriel Aracena
Lab 13 Flask application
'''

from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy

'''create an object 'app' from the Flask module
    __name__ set to __main__ if the script is running from the main file
'''

app =  Flask(__name__)

# connecting to postgresql
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:aracena@localhost/demoDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a db object
db = SQLAlchemy(app)

# create a secret key to handle data within our server
import os
app.config['SECRET_KEY']=os.urandom(24)

# define a model (create table in the 'demoDB' database)
class UserLogin(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), nullable = False)

# define a employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    employee_id = db.Column(db.String(20), unique= True, nullable = False)
    employee_name = db.Column(db.String(100), nullable = False)

# set the routing to the main page
# 'route' decorator is used to access the root URL
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='POST':
        return 'Successfully requested = ' + request.form['password']
    
    name = "Uriel"
    fruits = ['apple', 'orange', 'grapes']
    checkfruit = 'apple'
    return render_template('index.html', username=name, listfruits=fruits, checkedfruit=checkfruit)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        try:
            form = request.form
            emp_name = form['employee_name']
            emp_id = form['employee_id']

            # check if employee already exists by name (or use employee_id if that's unique)
            existing_employee = Employee.query.filter_by(employee_name=emp_name).first() # boolean (true,false)
            existing_id = Employee.query.filter_by(employee_id = emp_id).first() # boolean (true,false)

            if existing_employee:
                flash(f"Employee with name '{emp_name}' already exists!")
                flash(f"Employee with id '{emp_id}' already exists!")

            # create a new employee object and add form data into the database
            new_employee =  Employee(employee_id = emp_id, employee_name = emp_name)

            # store employee name in sesson
            session['employee1'] = new_employee.employee_name

            # add the new object to our database
            db.session.add(new_employee)
            db.session.commit()

            # message using flash
            flash(f'{request.form['employee_name']} successfully added!')
        except:
            flash('Fail to insert data! Try again')
    return render_template('users.html')

@app.route('/quotes')
def quotes():
    return redirect(url_for("index"))


# set the 'app' to run f you execute the file directly(not when its imported)
if __name__ == '__main__':
    with app.app_context():db.create_all()
    app.run(debug=True)