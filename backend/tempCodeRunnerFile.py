from models.order import Order
from app import db  # or wherever your SQLAlchemy `db` is initialized

# Ensure the database session is clean
db.session.rollback()

# Add sample orders
order1 = Order(id=1, product_id=1, quantity=2, status='Pending')
order2 = Order(id=2, product_id=1, quantity=2, status='Shipped')
order3 = Order(id=3, product_id=1, quantity=2, status='Delivered')

db.session.add_all([order1, order2, order3])
db.session.commit()
