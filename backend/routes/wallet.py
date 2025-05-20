from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Certificates

wallet_bp = Blueprint('wallet', __name__)

@wallet_bp.route('/my-certificates', methods=['GET'])
@jwt_required()
def my_certificates():
    user_id = get_jwt_identity()
    certs = list(Certificates.find({'owner': user_id}))
    for c in certs: c['id'] = str(c['_id'])
    return jsonify(certs), 200