from config import db

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum("pending", "fulfilled", "in_production"), default="pending")
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    product = db.relationship("Product", backref="orders")
