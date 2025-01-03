from models.user import User, db
from app import app  # Import your app instance

with app.app_context():
    user = User(username='1')
    user.set_password('1')  # Make sure this method is available
    db.session.add(user)
    db.session.commit()
    print("User created successfully")
