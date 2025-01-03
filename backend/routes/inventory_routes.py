from flask import Blueprint, jsonify, request
from models.inventory import Inventory
from models.product import Product

inventory_routes = Blueprint('inventory_routes', __name__)

@inventory_routes.route('/api/inventory', methods=['GET'])
def get_inventory():
    try:
        barcode = request.args.get('barcode')
        if barcode:
            # Join Inventory with Product to filter by barcode
            inventory = (
                Inventory.query.join(Product)
                .filter(Product.barcode == barcode)
                .all()
            )
        else:
            # Fetch all inventory records
            inventory = Inventory.query.all()
        
        if not inventory:
            return jsonify({'success': False, 'message': 'No inventory found.'}), 404

        inventory_list = [
            {
                'id': item.id,
                'product_id': item.product_id,
                'location': item.location,
                'quantity': item.quantity
            }
            for item in inventory
        ]
        return jsonify({'success': True, 'inventory': inventory_list})
    except Exception as e:
        print(f"Error fetching inventory: {e}")
        return jsonify({'success': False, 'message': 'Failed to fetch inventory'}), 500
