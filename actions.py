import os
import subprocess
import webbrowser

class Actions:

    def __init__(self):
        pass

    def execute(self, command: str):

        command = command.lower()

        if "open chrome" in command:
            subprocess.Popen("start chrome", shell=True)
            return "Opening Chrome."

        elif "open vscode" in command or "open visual studio code" in command:
            subprocess.Popen("code", shell=True)
            return "Opening VS Code."

        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")
            return "Opening YouTube."
        
        elif "open google" in command:
            webbrowser.open("https://google.com")
            return "Opening Google."

        elif "shutdown system" in command:
            os.system("shutdown /s /t 5")
            return "Shutting down system in 5 seconds."

        return None