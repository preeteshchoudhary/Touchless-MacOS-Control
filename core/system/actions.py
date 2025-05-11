import subprocess
import os

class SystemActions:
    def __init__(self):
        self.script_dir = os.path.join(os.path.dirname(__file__), "applescripts")
        
    def execute(self, action):
        script_path = os.path.join(self.script_dir, f"{action}.scpt")
        if os.path.exists(script_path):
            subprocess.run(['osascript', script_path], check=True)
            return True
        print(f"Action script not found: {action}")
        return False
