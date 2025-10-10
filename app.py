# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Learning Github Actions , AWS,DOCKER,EKS , making a simple project from scratch using perplexity ,."

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

# app.py
from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'yoursecretkey'  # Needed for session

# Sample products data
PRODUCTS = [
    {'id': 1, 'name': 'Book', 'price': 250},
    {'id': 2, 'name': 'Pen', 'price': 30},
    {'id': 3, 'name': 'Headphone', 'price': 1200}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    return render_template('products.html', products=PRODUCTS)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', [])
    cart.append(product_id)
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart_ids = session.get('cart', [])
    cart_items = [p for p in PRODUCTS if p['id'] in cart_ids]
    return render_template('cart.html', cart_items=cart_items)

@app.route('/order')
def order():
    session.pop('cart', None)
    return render_template('order.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
