from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client['certdb']

Users = db['users']
Certificates = db['certificates']
AuditLogs = db['audit_logs']