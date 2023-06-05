import pyautogui
from datetime import datetime
from io import BytesIO

class ScreenshotMaker:
    def __init__(self):
        self.name = datetime.now().strftime("%d%m%y_%H%M%S")

    def main(self):
        screenshot = pyautogui.screenshot()
    
        buffer = BytesIO()
        screenshot.save(buffer, format="PNG")
        buffer.seek(0)
    
    # Return the image data as a PNG file
        return buffer.getvalue()
