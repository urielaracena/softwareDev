
// Initialize cart from localStorage or create empty cart
let cart = JSON.parse(localStorage.getItem('dianasSalonCart')) || [];

// Initialize the cart badge counter
function updateCartBadge() {
    const cartCount = cart.reduce((total, item) => total + item.quantity, 0);
    document.getElementById('cartCountBadge').textContent = cartCount;
}

// Add item to cart
function addToCart(serviceId, serviceName, servicePrice) {
    // Check if item already exists in cart
    const existingItemIndex = cart.findIndex(item => item.id === serviceId);
    
    if (existingItemIndex !== -1) {
        // Item exists, increment quantity
        cart[existingItemIndex].quantity += 1;
    } else {
        // Item doesn't exist, add new item
        cart.push({
            id: serviceId,
            name: serviceName,
            price: servicePrice,
            quantity: 1
        });
    }
    
    // Save cart to localStorage
    saveCart();
    
    // Update cart badge
    updateCartBadge();
    
    // Show notification
    showNotification(`${serviceName} added to cart!`);
}

// Remove item from cart
function removeFromCart(serviceId) {
    // Find item index
    const itemIndex = cart.findIndex(item => item.id === serviceId);
    
    if (itemIndex !== -1) {
        // Remove item from cart
        cart.splice(itemIndex, 1);
        
        // Save cart to localStorage
        saveCart();
        
        // Update cart badge
        updateCartBadge();
        
        // If on cart page, refresh the cart display
        if (window.location.pathname.includes('/cart')) {
            renderCart();
        }
    }
}

// Update quantity of an item in cart
function updateQuantity(serviceId, newQuantity) {
    // Find item index
    const itemIndex = cart.findIndex(item => item.id === serviceId);
    
    if (itemIndex !== -1) {
        if (newQuantity <= 0) {
            // If quantity is 0 or less, remove item
            removeFromCart(serviceId);
        } else {
            // Update quantity
            cart[itemIndex].quantity = newQuantity;
            
            // Save cart to localStorage
            saveCart();
            
            // Update cart badge
            updateCartBadge();
            
            // If on cart page, refresh the cart display
            if (window.location.pathname.includes('/cart')) {
                renderCart();
            }
        }
    }
}

// Save cart to localStorage
function saveCart() {
    localStorage.setItem('dianasSalonCart', JSON.stringify(cart));
}

// Clear cart
function clearCart() {
    cart = [];
    saveCart();
    updateCartBadge();
    
    // If on cart page, refresh the cart display
    if (window.location.pathname.includes('/cart')) {
        renderCart();
    }
}

// Show notification
function showNotification(message) {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = 'alert alert-success alert-dismissible fade show position-fixed';
    notification.style.top = '70px';
    notification.style.right = '20px';
    notification.style.zIndex = '1050';
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    // Add to document
    document.body.appendChild(notification);
    
    // Auto dismiss after 3 seconds
    setTimeout(() => {
        notification.classList.remove('show');
        
        // Remove from DOM after animation
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Calculate cart total
function calculateCartTotal() {
    const subtotal = cart.reduce((total, item) => total + (item.price * item.quantity), 0);
    const taxRate = 0.08; // 8% tax
    const tax = subtotal * taxRate;
    const serviceCharge = 5.00; // Fixed $5 service charge
    const total = subtotal + tax + serviceCharge;
    
    return {
        subtotal: subtotal.toFixed(2),
        tax: tax.toFixed(2),
        serviceCharge: serviceCharge.toFixed(2),
        total: total.toFixed(2)
    };
}

// Render cart items on cart page
function renderCart() {
    const cartContainer = document.getElementById('cartItems');
    const cartSummary = document.getElementById('cartSummary');
    
    if (!cartContainer || !cartSummary) {
        return; // Not on cart page
    }
    
    if (cart.length === 0) {
        // Display empty cart message
        cartContainer.innerHTML = `
            <div class="empty-cart-message">
                <div class="empty-cart-icon">
                    <i class="fas fa-shopping-cart"></i>
                </div>
                <h3>Your cart is empty</h3>
                <p>You haven't added any services to your cart yet.</p>
                <a href="/services/hair" class="btn btn-primary mt-3">Browse Services</a>
            </div>
        `;
        
        cartSummary.style.display = 'none';
        
        // Hide checkout buttons
        const checkoutBtns = document.getElementById('checkoutButtons');
        if (checkoutBtns) {
            checkoutBtns.style.display = 'none';
        }
        
        return;
    }
    
    // Show cart summary
    cartSummary.style.display = 'block';
    
    // Show checkout buttons
    const checkoutBtns = document.getElementById('checkoutButtons');
    if (checkoutBtns) {
        checkoutBtns.style.display = 'block';
    }
    
    // Render cart items
    let cartHTML = '';
    
    cart.forEach(item => {
        cartHTML += `
            <div class="cart-item" data-id="${item.id}">
                <div class="row align-items-center">
                    <div class="col-md-6">
                        <h5>${item.name}</h5>
                        <p class="mb-0">$${item.price.toFixed(2)} each</p>
                    </div>
                    <div class="col-md-3">
                        <div class="input-group">
                            <button class="btn btn-outline-secondary" type="button" onclick="updateQuantity(${item.id}, ${item.quantity - 1})">-</button>
                            <input type="number" class="form-control text-center" value="${item.quantity}" min="1" onchange="updateQuantity(${item.id}, parseInt(this.value))">
                            <button class="btn btn-outline-secondary" type="button" onclick="updateQuantity(${item.id}, ${item.quantity + 1})">+</button>
                        </div>
                    </div>
                    <div class="col-md-2 text-end">
                        <p class="mb-0 fw-bold">$${(item.price * item.quantity).toFixed(2)}</p>
                    </div>
                    <div class="col-md-1 text-end">
                        <button class="btn btn-sm btn-outline-danger" onclick="removeFromCart(${item.id})">
                            <i class="fas fa-trash"></i>
                        </button>
                    </div>
                </div>
            </div>
        `;
    });
    
    cartContainer.innerHTML = cartHTML;
    
    // Update cart summary
    const totals = calculateCartTotal();
    
    document.getElementById('subtotal').textContent = `$${totals.subtotal}`;
    document.getElementById('tax').textContent = `$${totals.tax}`;
    document.getElementById('serviceCharge').textContent = `$${totals.serviceCharge}`;
    document.getElementById('total').textContent = `$${totals.total}`;
}

// Submit order
function submitOrder() {
    if (cart.length === 0) {
        showNotification('Cannot submit an empty order');
        return;
    }
    
    const totals = calculateCartTotal();
    
    // Send order data to server
    fetch('/submit_order', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            cart: cart,
            total: totals.total
        })
    })
    .then(response => response.json())
    .then(data => {
        // Clear cart
        clearCart();
        
        // Redirect to confirmation page
        window.location.href = `/confirmation/${data.order_number}`;
    })
    .catch(error => {
        console.error('Error submitting order:', error);
        showNotification('Error submitting order. Please try again.');
    });
}

// Initialize cart badge on page load
document.addEventListener('DOMContentLoaded', function() {
    updateCartBadge();
    
    // If on cart page, render cart
    if (window.location.pathname.includes('/cart')) {
        renderCart();
    }
});