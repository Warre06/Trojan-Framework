import pyautogui
from datetime import datetime

class ScreenshotMaker:
    def __init__(self):
        self.name = f'datetime.now().strftime("%d%m%y-%H%M%S").png'
    
    def main(self):
        screenshot = pyautogui.screenshot(self.name)
        return screenshot
