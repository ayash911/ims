from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from config import db


app = Flask(__name__, static_folder="../frontend/assets", template_folder="../frontend")

# Initialize CORS
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/ims'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize SQLAlchemy with the app
db.init_app(app)

# Initialize Migrate
migrate = Migrate(app, db)

# Serve frontend
@app.route("/")
def index():
    return send_from_directory(os.path.join(os.path.dirname(__file__), "../frontend/html"), "index.html")

@app.route("/html/<path:path>")
def serve_frontend(path):
    try:
        return send_from_directory(os.path.join(os.path.dirname(__file__), "../frontend/html"), path)
    except FileNotFoundError:
        return jsonify({'error': f'HTML file {path} not found'}), 404

@app.route("/assets/<path:path>")
def serve_static_files(path):
    try:
        return send_from_directory(os.path.join(os.path.dirname(__file__), "../frontend/assets"), path)
    except FileNotFoundError:
        return jsonify({'error': f'Static file {path} not found'}), 404

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Add product

# Import and register blueprints
from routes.product_routes import product_routes
from routes.order_routes import order_routes
from routes.inventory_routes import inventory_routes
from routes.auth_routes import auth_routes

# Register blueprints after initializing db
app.register_blueprint(product_routes)
app.register_blueprint(order_routes)
app.register_blueprint(auth_routes)
app.register_blueprint(inventory_routes)

if __name__ == "__main__":
    app.run(debug=True)
