import json
import os


class Memory:

    def __init__(self, path="memory.json"):
        self.path = path

        # Create file if it doesn't exist
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump({}, f)

    def load(self):

        try:
            with open(self.path, "r") as f:
                return json.load(f)

        except json.JSONDecodeError:
            # If file is empty or corrupted, reset it
            return {}

    def save(self, data):

        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)

    def remember(self, key, value):

        data = self.load()
        data[key] = value
        self.save(data)

    def recall(self, key):

        data = self.load()
        return data.get(key)