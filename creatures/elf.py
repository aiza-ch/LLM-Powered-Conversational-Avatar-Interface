import requests
from config import TOGETHER_API_KEY, TOGETHER_API_URL, MODEL_NAME

class Elf:
    def __init__(self):
        self.api_key = TOGETHER_API_KEY
        self.api_url = TOGETHER_API_URL
        self.model = MODEL_NAME
        self.personality_prefix = "You are a wise and graceful elf who speaks with elegance, kindness, and patience. Your words are poetic and thoughtful."
        self.chat_history = [
            {"role": "system", "content": self.personality_prefix}
        ]

    def introduce(self):
        return "✨ The graceful Elf bows. 'Welcome, traveler. How may I assist you in this enchanted realm?'"

    def respond(self, user_input):
        self.chat_history.append({"role": "user", "content": user_input})

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": self.chat_history,
            "temperature": 0.7,
            "max_tokens": 100
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=payload)

            if response.status_code != 200:
                return f"The elf remains silent... API error: {response.json().get('error', 'Unknown error')}"

            elf_reply = response.json()['choices'][0]['message']['content'].strip()
            self.chat_history.append({"role": "assistant", "content": elf_reply})

            return elf_reply

        except Exception as e:
            return f"The elf remains silent... Network error: {str(e)}"
