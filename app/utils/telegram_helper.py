# utils/telegram_helper.py

import requests
from config import TELEGRAM_BOT_BASE_URL,TELEGRAM_BOT_CHAT_ID

class TelegramHelper:
    def __init__(self):
        self.base_url = TELEGRAM_BOT_BASE_URL

    def send_message(self, message: str) -> dict:
        """Send a text message to a user or group by chat_id."""
        url = f"{self.base_url}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_BOT_CHAT_ID,
            "text": message,
            "parse_mode" : "HTML"
        }
        
        response = requests.post(url, data=payload)
        return response.json()

    def get_updates(self, offset: int = None) -> dict:
        """Fetch updates (messages sent to the bot)."""
        url = f"{self.base_url}/getUpdates"
        params = {}
        if offset:
            params["offset"] = offset
        response = requests.get(url, params=params)
        return response.json()
