from flask import Blueprint, jsonify
from models.product import Product

product_routes = Blueprint('product_routes', __name__)

@product_routes.route('/api/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        product_list = [{'id': p.id, 'name': p.name, 'barcode': p.barcode} for p in products]
        return jsonify(products=product_list)
    except Exception as e:
        print(f"Error fetching products: {e}")
        return jsonify({'error': 'Failed to fetch products'}), 500
