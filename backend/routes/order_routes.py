from flask import Blueprint, jsonify
from models.order import Order

order_routes = Blueprint('order_routes', __name__)


@order_routes.route('/api/orders', methods=['GET'])
def get_orders():
    try:
        orders = Order.query.all()
        order_list = [{'id': o.id, 'product_id': o.product_id, 'quantity': o.quantity, 'status': o.status} for o in orders]
        return jsonify(orders=order_list)
    except Exception as e:
        print(f"Error fetching orders: {e}")
        return jsonify({'error': 'Failed to fetch orders'}), 500
