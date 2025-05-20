from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from models import AuditLogs

audit_bp = Blueprint('audit', __name__)

@audit_bp.route('/audit-logs', methods=['GET'])
@jwt_required()
def audit_logs():
    logs = list(AuditLogs.find().sort('timestamp', -1))
    for l in logs: l['id'] = str(l['_id'])
    return jsonify(logs), 200