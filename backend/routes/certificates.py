import datetime
import os
from flask import Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Certificates, AuditLogs, Users
from utils.pdf_generator import generate_pdf
from utils.ipfs_client import upload_file
from utils.mock_blockchain  import anchor
from bson import ObjectId
import json
import qrcode
from io import BytesIO


cert_bp = Blueprint('certificates', __name__)

@cert_bp.route('/generate-certificates', methods=['POST'])
@jwt_required()
def generate_certificates():
    # handle bulk or single
    data = request.get_json()
    cert_id = Certificates.insert_one(data).inserted_id
    pdf_dir = os.path.join(os.getcwd(), "tmp")
    os.makedirs(pdf_dir, exist_ok=True)
    pdf_path = os.path.join(pdf_dir, f"{cert_id}.pdf")
    
    # Prepare data for QR (remove or convert ObjectId)
    qr_data = data.copy()
    qr_data['id'] = str(cert_id)  # Add id as string for QR
    # Do not include raw ObjectId
    if '_id' in qr_data:
        del qr_data['_id']

    # Generate QR code with certificate data as JSON
    qr_content = json.dumps(qr_data)
    qr = qrcode.make(qr_content)
    qr_bytes = BytesIO()
    try:
        qr.save(qr_bytes, format='PNG')
        qr_bytes.seek(0)
        qr_bytes.name = 'qrcode.png'
        print("QR bytes length:", len(qr_bytes.getvalue()))
    except Exception as e:
        print("QR code generation error:", e)
    
    generate_pdf(data, pdf_path, qr_bytes)
    # ipfs_hash = upload_file(pdf_path)
    # tx_hash = anchor(ipfs_hash, os.getenv('ETH_ACCOUNT'), os.getenv('ETH_KEY'))
    # Certificates.update_one({'_id': cert_id}, {'$set': {'ipfs': ipfs_hash, 'tx': tx_hash}})
    AuditLogs.insert_one({'user': get_jwt_identity(), 'action': 'generate', 'details': str(cert_id)})
    return jsonify({'id': str(cert_id)}), 200

@cert_bp.route('/verify/<cert_id>', methods=['GET'])
def verify(cert_id):
    try:
        cert = Certificates.find_one({'_id': ObjectId(cert_id)})
    except Exception:
        return jsonify({'valid': False, 'error': 'Invalid certificate ID'}), 400
    if not cert:
        return jsonify({'valid': False}), 404
    # optionally verify chain data
    return jsonify({
        'studentName': cert.get('name'),
        'issueDate': cert.get('date'),
        'course': cert.get('course'),
        'valid': True
    }), 200

@cert_bp.route('/generate-certificate', methods=['POST'])
@jwt_required()
def generate_event_certificate():
    data = request.get_json()
    student_id = get_jwt_identity()  # Get the logged-in user's ID
    cert_data = {
        'name': data.get('name'),
        'event': data.get('event'),
        'date': data.get('date'),
        'email': data.get('email'),
        'student_id': student_id,  # <-- Add this line
        # Add other fields as needed
    }
    cert_id = Certificates.insert_one(cert_data).inserted_id
    pdf_dir = os.path.join(os.getcwd(), "tmp")
    os.makedirs(pdf_dir, exist_ok=True)
    pdf_path = os.path.join(pdf_dir, f"{cert_id}.pdf")
    # ipfs_hash = upload_file(pdf_path)
    # tx_hash = anchor(ipfs_hash, os.getenv('ETH_ACCOUNT'), os.getenv('ETH_KEY'))
    # Certificates.update_one({'_id': cert_id}, {'$set': {'ipfs': ipfs_hash, 'tx': tx_hash}})

    # Generate QR code with certificate data as JSON
    qr_content = json.dumps(cert_data)
    qr = qrcode.make(qr_content)
    qr_bytes = BytesIO()
    try:
        qr.save(qr_bytes, format='PNG')
        qr_bytes.seek(0)
        qr_bytes.name = 'qrcode.png'
        print("QR bytes length:", len(qr_bytes.getvalue()))
    except Exception as e:
        print("QR code generation error:", e)
        
    generate_pdf(cert_data, pdf_path, qr_bytes)
    AuditLogs.insert_one({'name': f"{data.get('name')}_({data.get('name')})", 'event':  data.get('event'), 'details': str(cert_id), 'createdby_': get_jwt_identity(), 'createddate_': datetime.datetime.now()})
    return jsonify({'id': str(cert_id)}), 200

@cert_bp.route('/student/cert', methods=['GET'])
@jwt_required()
def get_student_certificates():
    try:
        user_id = get_jwt_identity()
        print(user_id)
        user = Users.find_one({'_id': ObjectId(user_id)})
        print(user)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        email = user['email'].strip().lower()
        certificates = list(Certificates.find({'email': email}))
        print("Filtering certificates for email:", email)
        print("Certificates found:", certificates)

        cert_list = []
        for cert in certificates:
            cert_data = {
                'id': str(cert['_id']),
                'name': cert.get('name'),
                'event': cert.get('event'),
                'date': cert.get('date'),
                'email': cert.get('email'),
            }
            cert_list.append(cert_data)

        return jsonify({'certificates': cert_list}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
