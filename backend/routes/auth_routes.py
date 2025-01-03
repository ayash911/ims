from flask import Blueprint, request, jsonify

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/register', methods=['POST'])
def register():
    from models.user import User, db  # Import inside the route to avoid circular import
    
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username and password:
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    
    return jsonify({'error': 'Invalid input'}), 400
