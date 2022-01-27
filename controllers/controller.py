from flask import render_template
from app import app
from models.list_all_orders import orders


@app.route('/orders')
def index():
    return render_template('index.html', title="Home" ,orders=orders)

@app.route('/orders/<index>')
def get_one_order(index):
    order = orders[int(index)]
    return render_template('order.html', order=order )

    