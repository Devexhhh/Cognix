import subprocess
import webbrowser
import os

class Actions:

    def execute(self, action):

        if action == "open_chrome":
            subprocess.Popen("start chrome", shell=True)
            return "Opening Chrome."

        elif action == "open_youtube":
            webbrowser.open("https://youtube.com")
            return "Opening YouTube."

        elif action == "open_google":
            webbrowser.open("https://google.com")
            return "Opening Google."

        elif action == "open_vscode":
            subprocess.Popen("code", shell=True)
            return "Opening VS Code."

        return None