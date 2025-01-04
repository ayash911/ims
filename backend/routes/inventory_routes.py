from flask import Blueprint, jsonify, request
from models import Inventory, Product

inventory_routes = Blueprint("inventory_routes", __name__)

@inventory_routes.route("/api/inventory", methods=["GET"])
def get_inventory():
    try:
        barcode = request.args.get("barcode")
        query = Inventory.query.join(Product)
        if barcode:
            query = query.filter(Product.barcode == barcode)
        inventory = query.all()

        if not inventory:
            return jsonify({"success": False, "message": "No inventory found."}), 404

        inventory_list = [
            {
                "id": item.id,
                "product_id": item.product_id,
                "location": item.location,
                "quantity": item.quantity
            } for item in inventory
        ]
        return jsonify({"success": True, "inventory": inventory_list})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
