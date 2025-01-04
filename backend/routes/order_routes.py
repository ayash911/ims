from flask import Blueprint, jsonify, request
from models import Order, Customer
from config import db

order_routes = Blueprint("order_routes", __name__)

@order_routes.route("/api/orders", methods=["GET"])
def get_orders():
    try:
        orders = Order.query.all()
        orders_list = [
            {
                "id": order.id,
                "customer_id": order.customer_id,
                "product_id": order.product_id,
                "quantity": order.quantity,
                "status": order.status,
                "created_at": order.created_at
            } for order in orders
        ]
        return jsonify({"success": True, "orders": orders_list})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@order_routes.route("/api/add_order", methods=["POST"])
def add_order():
    try:
        data = request.json
        order = Order(
            customer_id=data["customer_id"],
            product_id=data["product_id"],
            quantity=data["quantity"],
            status=data.get("status", "Pending"),
            created_at=data["created_at"]
        )
        db.session.add(order)

        # Update customer total_pcs_bought
        customer = Customer.query.get(data["customer_id"])
        if customer:
            customer.total_pcs_bought += data["quantity"]

        db.session.commit()
        return jsonify({"success": True, "message": "Order added successfully."}), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
