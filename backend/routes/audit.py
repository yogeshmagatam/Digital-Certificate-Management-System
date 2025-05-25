from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from models import AuditLogs, Users
from bson import ObjectId

audit_bp = Blueprint('audit', __name__)

@audit_bp.route('/audit-logs', methods=['GET'])
@jwt_required()
def audit_logs():
    logs = list(AuditLogs.find().sort('timestamp', -1))
    for l in logs:
        l['id'] = str(l['_id'])
        del l['_id']  # Remove the ObjectId field to avoid serialization error
    # Lookup user info
        user_id = l.get('user')
        user = Users.find_one({'_id': ObjectId(user_id)}) if user_id else None
        l['user'] = user.get('email') if user and user.get('email') else str(user_id)
        l['CreatedBy_'] = user.get('email') if user and user.get('email') else str(user_id)
    return jsonify(logs), 200