import os
from dotenv import load_dotenv


load_dotenv()

# DB_URI = os.getenv('DB_URI')
# AUTH_EMAIL = os.getenv('AUTH_EMAIL')
# AUTH_PWD = os.getenv('AUTH_PWD')
# SEND_EMAIL_TO = os.getenv('SEND_EMAIL_TO')

TELEGRAM_BOT_BASE_URL = os.getenv('TELEGRAM_BOT_BASE_URL')
TELEGRAM_BOT_CHAT_ID = os.getenv('TELEGRAM_BOT_CHAT_ID')