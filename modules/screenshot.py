import pyautogui
from datetime import datetime

class ScreenshotMaker:
    def __init__(self):
        self.name = datetime.now().strftime("%d%m%y-%H%M%S")
    
    def main(self):
        screenshot = pyautogui.screenshot(self.name)
        return screenshot
