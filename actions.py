import webbrowser
import time
import psutil
import os

class ActionController:
    def __init__(self, cooldown=3.0):
        """
        Initializes the action controller with a cooldown timer.
        """
        self.cooldown = cooldown
        self.last_action_time = 0
        self.current_action = "None"

    def perform_action(self, fingers_count):
        """
        Maps the finger count to a specific action if the cooldown has passed.
        """
        current_time = time.time()
        
        # Check if enough time has passed since the last action
        if current_time - self.last_action_time > self.cooldown:
            try:
                if fingers_count == 1:
                    print("Action: Opening Claude AI...")
                    webbrowser.open('https://claude.ai')
                    self.current_action = "Opened Claude"
                    self.last_action_time = current_time

                elif fingers_count == 2:
                    print("Action: Opening ChatGPT...")
                    webbrowser.open('https://chat.openai.com')
                    self.current_action = "Opened ChatGPT"
                    self.last_action_time = current_time

                elif fingers_count == 3:
                    print("Action: Opening Gemini...")
                    webbrowser.open('https://gemini.google.com')
                    self.current_action = "Opened Gemini"
                    self.last_action_time = current_time

                elif fingers_count == 4:
                    print("Action: Opening LinkedIn...")
                    webbrowser.open('https://linkedin.com')
                    self.current_action = "Opened LinkedIn"
                    self.last_action_time = current_time

                elif fingers_count == 0:
                    print("Action: Closing browsers...")
                    self.close_browsers()
                    self.current_action = "Closed Browsers"
                    self.last_action_time = current_time
                    
            except Exception as e:
                print(f"Error performing action: {e}")
                
        return self.current_action

    def close_browsers(self):
        """
        Iterates through running processes and terminates major browsers.
        """
        browser_processes = ['chrome.exe', 'msedge.exe', 'firefox.exe', 'brave.exe', 'Google Chrome', 'Safari']
        
        for proc in psutil.process_iter(['name']):
            try:
                if proc.info['name'] in browser_processes:
                    proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass