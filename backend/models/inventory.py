from config import db

class Inventory(db.Model):
    __tablename__ = "inventory"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    location = db.Column(db.Enum("manufacturing", "warehouse", "loading_area"), nullable=False)
    quantity = db.Column(db.Integer, default=0)

    product = db.relationship("Product", backref="inventory")
