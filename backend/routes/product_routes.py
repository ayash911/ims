from flask import  jsonify, request, Blueprint
from models import Product
from config import db
from barcode_generator import generate_barcode
import pytz

product_routes = Blueprint('product_routes', __name__)


@product_routes.route("/api/products", methods=["GET"])
def get_products():
    try:
        products = Product.query.all()  # Fetch all products from the database
        product_list = [{
            "id": product.id,
            "name": product.name,
            "barcode": product.barcode,
            "grade": product.grade,
            "thickness": product.thickness,
            "dimension": product.dimension,
            "item_id": product.item_id,
            "date": product.created_at
        } for product in products]

        return jsonify({"products": product_list})

    except Exception as e:
        print(e)
        return jsonify({"error": "Unable to fetch products"}), 500


from datetime import datetime
@product_routes.route("/api/add_product", methods=["POST"])
def add_product():
    data = request.json
    print("Received data:", data)  # Debugging line
    
    try:
        # Validate incoming data
        if not all(k in data for k in ("grade", "thickness", "dimension")):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Get the current date (in ddmmyy format)
        date_today = datetime.now(pytz.timezone('Asia/Kathmandu')).strftime('%d%m%y')
        
        barcode = generate_barcode(
            grade=data["grade"],
            thickness=data["thickness"],
            dimension=data["dimension"],

        )

        # Create a new product instance
        product = Product(
            name=barcode,
            barcode=barcode,
            grade=data["grade"],
            thickness=data["thickness"],
            dimension=data["dimension"],
            item_id=0,            
            created_at=date_today
        )
        
        # Add to the database
        db.session.add(product)
        db.session.commit()

        return jsonify({"message": "Product added successfully", "barcode": barcode}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
