from flask import request, jsonify
from functools import wraps
from app.db import mongo

# --- Auth decorator ---
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Token sent in header
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            parts = auth_header.split()
            if len(parts) == 2 and parts[0] == "Bearer":
                token = parts[1]

        if not token:
            return jsonify({"error": "Token is missing"}), 401

        # Check token in users collection
        user = mongo.db.users.find_one({"token": token})
        if not user:
            return jsonify({"error": "Invalid token"}), 401

        # Attach user info to request if needed
        request.user = user
        return f(*args, **kwargs)
    return decorated
