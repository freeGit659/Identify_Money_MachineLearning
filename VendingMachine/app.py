from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Danh sách các loại đồ uống
drinks = [
    {"id": 1, "name": "Coca Cola", "image": "cola.jpg", "price": 10, 'quantity': 1},
    {"id": 2, "name": "Pepsi", "image": "pepsi.jpg", "price": 13, 'quantity': 0},
    {"id": 3, "name": "Water", "image": "water.jpg", "price": 5, 'quantity': 0},
    {"id": 4, "name": "Aqua", "image": "water.jpg", "price": 9, 'quantity': 0},
    # Thêm các loại đồ uống khác tại đây
]

# Giỏ hàng
cart = []
total = 0;


@app.route('/')
def index():
    return render_template('index.html', drinks=drinks, cart=cart, total=total)


@app.route('/add_to_cart/<int:drink_index>')
def add_to_cart(drink_index):
    global total
    drink = drinks[drink_index]
    drink['quantity'] += 1
    total += drink['quantity'] * drink['price']
    for item in cart:
        if item['id'] == drink['id']:
            item['quantity'] = drink['quantity']
            return redirect(url_for('index'))
    cart.append(drink.copy())
    return redirect(url_for('index'))


@app.route('/remove_from_cart/<int:cart_index>')
def remove_from_cart(cart_index):
    for drink in drinks:
        if drink['id'] == cart[cart_index]['id']:
            drink['quantity'] = 0
    del cart[cart_index]
    return redirect(url_for('index'))


@app.route('/clear_cart')
def clear_cart():
    cart.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
