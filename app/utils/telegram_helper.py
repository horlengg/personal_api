# utils/telegram_helper.py

import requests

class TelegramHelper:
    def __init__(self):
        self.bot_token = "8343350308:AAHh8ovjZc19ujmtp79lsoNwHVKPSxVVxo4"
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}"
        self.chat_id = "1756952475"

    def send_message(self, message: str) -> dict:
        """Send a text message to a user or group by chat_id."""
        url = f"{self.base_url}/sendMessage"
        payload = {
            "chat_id": self.chat_id,
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
