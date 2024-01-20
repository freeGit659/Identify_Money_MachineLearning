from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Danh sách các loại đồ uống
drinks = [
    {"name": "Coca Cola", "image": "cola.jpg", "price": 10},
    {"name": "Pepsi", "image": "pepsi.jpg", "price": 13},
    {"name": "Water", "image": "water.jpg", "price": 5},
    {"name": "Aqua", "image": "water.jpg", "price": 9},
    # Thêm các loại đồ uống khác tại đây
]

# Giỏ hàng
cart = []


@app.route('/')
def index():
    return render_template('index.html', drinks=drinks, cart=cart)


@app.route('/add_to_cart/<int:drink_index>')
def add_to_cart(drink_index):
    drink = drinks[drink_index]
    cart.append(drink.copy())
    return redirect(url_for('index'))


@app.route('/remove_from_cart/<int:cart_index>')
def remove_from_cart(cart_index):
    del cart[cart_index]
    return redirect(url_for('index'))


@app.route('/clear_cart')
def clear_cart():
    cart.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
