import pyautogui
from datetime import datetime

class ScreenshotMaker:
    def __init__(self):
        self.screenshot_folder = "screenshots/"
    
    def start(self):
        screenshot = pyautogui.screenshot()
        current_time = datetime.now().strftime("%d%m%y-%H%M%S")
        screenshot_path = f'screenshots/screenshot_{current_time}.png'
        screenshot.save(screenshot_path)


screenshot = ScreenshotMaker()
screenshot.start()
