import os
from flask import Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Certificates, AuditLogs
from utils.pdf_generator import generate_pdf
from utils.ipfs_client import upload_file
from utils.mock_blockchain  import anchor

cert_bp = Blueprint('certificates', __name__)

@cert_bp.route('/generate-certificates', methods=['POST'])
# @jwt_required()
def generate_certificates():
    # handle bulk or single
    data = request.get_json()
    cert_id = Certificates.insert_one(data).inserted_id
    pdf_path = f"/tmp/{cert_id}.pdf"
    generate_pdf(data, pdf_path)
    ipfs_hash = upload_file(pdf_path)
    tx_hash = anchor(ipfs_hash, os.getenv('ETH_ACCOUNT'), os.getenv('ETH_KEY'))
    Certificates.update_one({'_id': cert_id}, {'$set': {'ipfs': ipfs_hash, 'tx': tx_hash}})
    AuditLogs.insert_one({'user': get_jwt_identity(), 'action': 'generate', 'details': str(cert_id)})
    return jsonify({'id': str(cert_id)}), 200

@cert_bp.route('/verify/<cert_id>', methods=['GET'])
def verify(cert_id):
    cert = Certificates.find_one({'_id': cert_id})
    if not cert:
        return jsonify({'valid': False}), 404
    # optionally verify chain data
    return jsonify({
        'studentName': cert['name'],
        'issueDate': cert['date'],
        'course': cert['course'],
        'valid': True
    }), 200