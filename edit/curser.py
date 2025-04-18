import math
import random
import time
from selenium.webdriver.common.action_chains import ActionChains

class Curser:
    def __init__(self, driver):
        """
        Initialize the Curser with a Selenium WebDriver instance.
        :param driver: Selenium WebDriver instance
        """
        self.driver = driver

    def __call__(self, element):
        """
        Allow the Curser instance to be called directly with an element.
        :param element: Selenium WebElement to move the cursor to and click
        """
        self.move_cursor(element)

    def move_cursor(self, element):
        """
        Move the cursor to the center of the specified element with randomized paths and detours,
        and perform a click once the cursor reaches the target.
        :param element: Selenium WebElement to move the cursor to
        """
        try:
            location = element.location
            size = element.size
            start_x, start_y = self.get_cursor_position()
            end_x = location['x'] + size['width'] / 2
            end_y = location['y'] + size['height'] / 2

            duration = random.uniform(0.3, 4.0)
            steps = int(duration * 30)
            detour_chance = 0.25 if duration <= 1.5 else 0.05
            detour_enabled = random.random() < detour_chance

            # Generate path with detours
            path = self.generate_path(start_x, start_y, end_x, end_y, steps, detour_enabled)

            # Move cursor along the path
            for x, y in path:
                self.driver.execute_script(f"""
                    const cursor = document.getElementById('customCursor');
                    if (cursor) {{
                        cursor.style.left = "{x}px";
                        cursor.style.top = "{y}px";
                    }}
                """)
                time.sleep(duration / steps)

            # If detour occurred, finalize movement to the target
            if detour_enabled:
                self.driver.execute_script(f"""
                    const cursor = document.getElementById('customCursor');
                    if (cursor) {{
                        cursor.style.left = '{end_x}px';
                        cursor.style.top = '{end_y}px';
                    }}
                """)
                time.sleep(0.2)

            # Perform the click at the target
            ActionChains(self.driver).move_to_element(element).click().perform()
            print(f"✅ Clicked on element at ({end_x}, {end_y})")

        except Exception as e:
            print(f"Error in move_cursor: {e}")

    def generate_path(self, start_x, start_y, end_x, end_y, steps, detour_enabled):
        """
        Generate a randomized path from start to end with optional detours.
        """
        path = []
        for i in range(steps + 1):
            t = i / steps
            x = start_x + (end_x - start_x) * t
            y = start_y + (end_y - start_y) * t

            # Add detour logic
            if detour_enabled and random.random() < 0.1:
                angle = random.uniform(-math.pi / 4, math.pi / 4)
                radius = random.uniform(10, 50)
                x += radius * math.cos(angle)
                y += radius * math.sin(angle)

            path.append((x, y))
        return path

    def get_cursor_position(self):
        """
        Get the current position of the cursor.
        """
        return 0, 0  # Default starting position (can be enhanced if needed)
