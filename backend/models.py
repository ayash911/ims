from config import db
from datetime import datetime
import pytz

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    barcode = db.Column(db.String(255), unique=True, nullable=False)
    grade = db.Column(db.String(1), nullable=False)
    thickness = db.Column(db.String(10), nullable=False)
    dimension = db.Column(db.String(10), nullable=False)
    item_id = db.Column(db.Integer, autoincrement=True, nullable=False)  # Auto-increment
    created_at = db.Column(db.String(6), nullable=False, default=datetime.now(pytz.timezone('Asia/Kathmandu')).strftime('%d%m%y'))  # Auto date


class Inventory(db.Model):
    __tablename__ = "inventory"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    location = db.Column(db.Enum("manufacturing", "warehouse", "loading_area"), nullable=False)
    quantity = db.Column(db.Integer, default=0)

    product = db.relationship("Product", backref="inventory")

class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    total_pcs_bought = db.Column(db.Integer, default=0)

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum("Pending", "Completed", "Cancelled"), nullable=False, default="Pending")
    created_at = db.Column(db.DateTime, nullable=False)

    customer = db.relationship("Customer", backref="orders")
    product = db.relationship("Product", backref="orders")
