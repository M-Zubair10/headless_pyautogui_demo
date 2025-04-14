import pyautogui
import time

def main():
    # Give some time to switch to the target window if needed
    print("Starting PyAutoGUI test in 3 seconds...")
    time.sleep(3)
    
    # Get screen size
    screen_width, screen_height = pyautogui.size()
    print(f"Screen size: {screen_width}x{screen_height}")
    
    # Move mouse to center of screen
    center_x = screen_width // 2
    center_y = screen_height // 2
    print(f"Moving mouse to center: ({center_x}, {center_y})")
    pyautogui.moveTo(center_x, center_y, duration=1)
    
    # Take a screenshot
    print("Taking screenshot...")
    screenshot = pyautogui.screenshot()
    screenshot.save("test_screenshot.png")
    print("Screenshot saved as test_screenshot.png")
    
    # Type some text
    print("Typing text...")
    pyautogui.write("Hello from PyAutoGUI in Docker!", interval=0.1)
    
    print("Test completed successfully!")

if __name__ == "__main__":
    main() 