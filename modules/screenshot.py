import pyautogui
from datetime import datetime

class ScreenshotMaker:
    def __init__(self):
        self.name = datetime.now().strftime("%d%m%y_%H%M%S")

    def main(self):
        screenshot_path = f"{self.name}.png"
        screenshot = pyautogui.screenshot(screenshot_path)
        return screenshot
