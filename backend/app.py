from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET
CORS(app)
jwt = JWTManager(app)

# Register Blueprints
from routes.auth import auth_bp
from routes.certificates import cert_bp
from routes.wallet import wallet_bp
from routes.audit import audit_bp

app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(cert_bp, url_prefix='/api')
app.register_blueprint(wallet_bp, url_prefix='/api')
app.register_blueprint(audit_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)