import datetime
import os
import hashlib
from flask import Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Certificates, AuditLogs, Users
from utils.pdf_generator import generate_pdf
from utils.ipfs_client import upload_file
from utils.mock_blockchain  import anchor
from utils.blockchain import anchor_certificate, is_certificate_anchored
from bson import ObjectId
import json
import qrcode
from io import BytesIO
from web3 import Web3
import copy

cert_bp = Blueprint('certificates', __name__)

def serialize_cert(cert):
    cert = copy.deepcopy(cert)
    cert['id'] = str(cert['_id'])
    del cert['_id']
    return cert

@cert_bp.route('/generate-certificates', methods=['POST'])
@jwt_required()
def generate_certificates():
    data = request.get_json()
    
    if 'template_type' in data:
        data['template_type'] = int(data['template_type'])
    
    existing_cert = Certificates.find_one({
        'name': data.get('name'),
        'course': data.get('course'),
        'date': data.get('date')
    })
    
    if existing_cert:
        return jsonify({
            'error': 'Certificate already exists',
            'id': str(existing_cert['_id'])
        }), 409

    cert_id = Certificates.insert_one(data).inserted_id
    
    pdf_dir = os.path.join(os.getcwd(), "tmp")
    os.makedirs(pdf_dir, exist_ok=True)
    pdf_path = os.path.join(pdf_dir, f"{cert_id}.pdf")
    
    
    qr_data = data.copy()
    qr_data['id'] = str(cert_id) 
   
    if '_id' in qr_data:
        del qr_data['_id']

    
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
    
    generate_pdf(data, pdf_path, qr_bytes, template_type=data.get('template_type', 1))
    
    name = data.get('email').split('@')[0]
    AuditLogs.insert_one({'name': name, 'event': data.get('event'), 'action': 'generate', 'details': str(cert_id), 'user': get_jwt_identity(), 'CreatedBy_': get_jwt_identity(), 'CreatedDate_': datetime.datetime.now()})
    return jsonify({'id': str(cert_id)}), 200

@cert_bp.route('/verify/<cert_id>', methods=['GET'])
def verify(cert_id):
    try:
        cert = Certificates.find_one({'_id': ObjectId(cert_id)})
    except Exception:
        return jsonify({'valid': False, 'error': 'Invalid certificate ID'}), 400
    if not cert:
        return jsonify({'valid': False}), 404
    cert_hash = hashlib.sha256(json.dumps(cert, sort_keys=True).encode()).hexdigest()
    anchored = is_certificate_anchored(Web3.to_bytes(hexstr=cert_hash))
    return jsonify({
        'studentName': cert.get('name'),
        'issueDate': cert.get('date'),
        'course': cert.get('course'),
        'anchored': anchored,
        'valid': anchored
    }), 200

@cert_bp.route('/generate-certificate', methods=['POST'])
@jwt_required()
def generate_event_certificate():
    data = request.get_json()
    student_id = get_jwt_identity()  
    existing_cert = Certificates.find_one({
        'name': data.get('name'),
        'event': data.get('event'),
        'date': data.get('date'),
        'email': data.get('email'),
        'template_type': data.get('template_type', 1)
    })
    
    if existing_cert:
        return jsonify({
            'error': 'Certificate already exists for this event',
            'id': str(existing_cert['_id'])
        }), 409
        
    cert_data = {
        'name': data.get('name'),
        'event': data.get('event'),
        'date': data.get('date'),
        'email': data.get('email'),
        'student_id': student_id,
        'template_type': data.get('template_type', 1), 
    }
    cert_id = Certificates.insert_one(cert_data).inserted_id
    pdf_dir = os.path.join(os.getcwd(), "tmp")
    os.makedirs(pdf_dir, exist_ok=True)
    pdf_path = os.path.join(pdf_dir, f"{cert_id}.pdf")
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
        
    generate_pdf(cert_data, pdf_path, qr_bytes, template_type=data.get('template_type', 1))
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

@cert_bp.route('/download/<cert_id>', methods=['GET'])
@jwt_required()
def download_certificate(cert_id):
    try:
        cert = Certificates.find_one({'_id': ObjectId(cert_id)})
        if not cert:
            return jsonify({'error': 'Certificate not found'}), 404
        user_id = get_jwt_identity()
        user = Users.find_one({'_id': ObjectId(user_id)})
        if not user or (user.get('role') != 'admin' and user['email'].lower() != cert.get('email', '').lower()):
            return jsonify({'error': 'Unauthorized access'}), 403
        pdf_dir = os.path.join(os.getcwd(), "tmp")
        pdf_path = os.path.join(pdf_dir, f"{cert_id}.pdf")
        
        if not os.path.exists(pdf_path):
            os.makedirs(pdf_dir, exist_ok=True)
            qr_data = cert.copy()
            qr_data['id'] = str(cert['_id'])
            if '_id' in qr_data:
                del qr_data['_id']
            
            qr_content = json.dumps(qr_data)
            qr = qrcode.make(qr_content)
            qr_bytes = BytesIO()
            qr.save(qr_bytes, format='PNG')
            qr_bytes.seek(0)
            qr_bytes.name = 'qrcode.png'
            
            generate_pdf(cert, pdf_path, qr_bytes, template_type=cert.get('template_type', 1))

        AuditLogs.insert_one({
            'user': get_jwt_identity(),
            'action': 'download',
            'details': str(cert_id),
            'timestamp': datetime.datetime.now()
        })
        
        return send_file(
            pdf_path,
            mimetype='application/pdf',
            as_attachment=True,
            download_name=f"certificate_{cert.get('name')}_{cert.get('event')}.pdf"
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
