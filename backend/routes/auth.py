from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import Users
import bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return '', 200
    data = request.get_json()
    user = Users.find_one({'email': data['email']})
    if user and bcrypt.checkpw(data['password'].encode('utf-8'), user['password']):
        token = create_access_token(identity=str(user['_id']))
        role = user.get('role', 'student')  
        return jsonify({'token': token, 'role': role}), 200
    return jsonify({'msg': 'Bad credentials'}), 401


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    Users.insert_one({'email': data['email'], 'password': hashed, 'role': data.get('role', 'student'), 'fullName': data.get('fullName')})
    return jsonify({'msg': 'User registered'}), 201
