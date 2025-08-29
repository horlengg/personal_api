from flask import Blueprint, request
from app.utils import get_client_ip,is_localhost
# from app.db import mongo
from user_agents import parse
# from app.utils import send_email
# import secrets
from app.utils import TelegramHelper


api_bp = Blueprint("api", __name__)

@api_bp.route('/view',methods=["POST"])
def web_porfolio_view():
    try :
        ua_string = request.headers.get('User-Agent')
        user_agent = parse(ua_string)
        browser = user_agent.browser.family
        os = user_agent.os.family
        device = user_agent.device.family

        request_data = request.get_json()
        url = request_data.get("url")
        
        if url is None:
            return "...", 400
        
        if is_localhost(url):
            return "Done",200
        
        data = {
            "url" : url,
            "device" : f'Browser: {browser}, OS: {os}, Device: {device}',
            "ip_address" : get_client_ip()
        }

        info = f"""
Heyyyy , a user visited your website!.

data : 

<pre>
{{
"url": "{data['url']}",
"device": "{data['device']}",
"ip_address": "127.0.0.1"
}}
</pre>
            """

        telegram = TelegramHelper()
        # telegram.send_message(message="")
        telegram.send_message(message=info)

        # send_email(info)
        # collection = mongo.db.portfolio_client_view
        # collection.delete_many({})
        # collection.insert_one(data)
        return "Done",200
    except Exception as e:
        return str(e), 400
    
# @api_bp.route('/view',methods=["GET"])
# @token_required
# def web_porfolio_view_list():
#     try :
#         collection = mongo.db.portfolio_client_view
#         views_cursor = collection.find().limit(100)
#         views_list = list(views_cursor)
#         for view in views_list:
#             view["_id"] = str(view["_id"])
#         return jsonify(views_list), 200
#     except Exception as e:
#         return str(e), 400


# @api_bp.route('/users', methods=["POST"])
# @token_required
# def create_user():
#     # mongo.db.users.delete_many({})
#     data = request.get_json()
#     email = data.get("email")
#     pwd = data.get("pwd")

#     if not email or not pwd:
#         return jsonify({"error": "Email and password are required"}), 400

#     # Check if user already exists
#     if mongo.db.users.find_one({"email": email}):
#         return jsonify({"error": "User already exists"}), 400

#     # Hash password
#     hashed_pwd = bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt())

#     # Insert user into DB
#     mongo.db.users.insert_one({
#         "email": email,
#         "pwd": hashed_pwd.decode('utf-8')
#     })

#     return jsonify({"message": "User created successfully"}), 201

# # --- Get all users ---
# @api_bp.route('/users', methods=["GET"])
# @token_required
# def get_all_users():
#     users_cursor = mongo.db.users.find()
#     users_list = []
#     for user in users_cursor:
#         users_list.append({
#             "id": str(user["_id"]),
#             "email": user["email"],
#             "pwd": user["pwd"],
#         })
#     return jsonify(users_list), 200

# @api_bp.route('/login', methods=["POST"])
# def login():
#     data = request.get_json()
#     email = data.get("email")
#     pwd = data.get("pwd")

#     if not email or not pwd:
#         return jsonify({"error": "Email and password are required"}), 400

#     # Find user
#     user = mongo.db.users.find_one({"email": email})
#     if not user:
#         return jsonify({"error": "Invalid credentials"}), 401

#     # Check password
#     if not bcrypt.checkpw(pwd.encode('utf-8'), user["pwd"].encode('utf-8')):
#         return jsonify({"error": "Invalid credentials"}), 401

#     # Generate a new token (overwrite previous if exists)
#     token = secrets.token_hex(16)  # 32-character hex token
#     mongo.db.users.update_one(
#         {"_id": user["_id"]},
#         {"$set": {"token": token}}
#     )

#     return jsonify({"token": token}), 200