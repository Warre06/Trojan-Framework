import pyautogui
from datetime import datetime
from io import BytesIO

class ScreenshotMaker:
    def __init__(self):
        self.name = datetime.now().strftime("%d%m%y_%H%M%S")

    def main(self):
        screenshot_path = f"{self.name}.png"
        screenshot = pyautogui.screenshot(screenshot_path)
        
        buffer = BytesIO()
        screenshot.save(buffer, format="PNG")
        buffer.seek(0)
        
        # Return the image data
        return buffer.getvalue()
