import ollama
from config import MODEL_NAME, SYSTEM_PROMPT

class Brain:

    def __init__(self):
        self.messages = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

    def think(self, user_input):

        self.messages.append({
            "role": "user",
            "content": user_input
        })

        response = ollama.chat(
            model=MODEL_NAME,
            messages=self.messages
        )

        reply = response['message']['content']

        self.messages.append({
            "role": "assistant",
            "content": reply
        })

        return reply