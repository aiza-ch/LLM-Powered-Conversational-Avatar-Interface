import requests
from config import TOGETHER_API_KEY, TOGETHER_API_URL, MODEL_NAME

class Dragon:
    def __init__(self):
        self.api_key = TOGETHER_API_KEY
        self.api_url = TOGETHER_API_URL
        self.model = MODEL_NAME
        self.personality_prefix = "You are a mighty dragon who is ancient, proud, and fierce. Speak in a grand and intimidating tone."
        self.chat_history = [
            {"role": "system", "content": self.personality_prefix}
        ]

    def introduce(self):
        return "The mighty Dragon roars! 'Who dares to disturb my slumber?'"

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
                return f"The dragon is silent... API error: {response.json().get('error', 'Unknown error')}"

            dragon_reply = response.json()['choices'][0]['message']['content'].strip()
            self.chat_history.append({"role": "assistant", "content": dragon_reply})

            return dragon_reply

        except Exception as e:
            return f"The dragon is silent... Network error: {str(e)}"

