import time
import random
from selenium.webdriver.common.by import By  # Import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def generate_human_scroll_pattern(max_scroll):
    """
    Generate a human-like scroll pattern that accelerates toward the middle and decelerates after.
    """
    steps = random.randint(6, 10)  # Randomize the number of steps
    half = steps // 2
    pattern = []

    for i in range(steps):
        if i <= half:
            ratio = i / half  # Accelerate
        else:
            ratio = (steps - i) / half  # Decelerate
        distance = int(max_scroll * ratio * random.uniform(0.8, 1))  # Add randomness to the distance
        pattern.append(distance)
    return pattern

def human_like_scroll(driver, direction='down', total_scrolls=10):
    """
    Perform human-like scrolling behavior in the browser.

    Parameters:
    - driver: Selenium WebDriver instance
    - direction: 'down' or 'up'
    - total_scrolls: Number of scroll sequences to perform
    """
    for _ in range(total_scrolls):
        max_scroll = random.randint(40, 250)  # Randomize the maximum scroll distance
        print(f"Performing scroll with max_scroll: {max_scroll}")
        pattern = generate_human_scroll_pattern(max_scroll)
        for dist in pattern:
            delta = dist if direction == 'down' else -dist
            driver.execute_script(f"window.scrollBy(0, {delta});")
            time.sleep(0.05)  # Short pause between each scroll step
        time.sleep(random.uniform(0.3,1))  # Longer pause between scroll sequences for human-like behavior

def scroll_until_visible(driver, by, value, container=None):
    """
    Scrolls the page or a specific container until the specified element's center is visible.
    If the element's center is already visible, no scrolling is performed.
    If the page reaches the bottom, it scrolls back up and retries.
    """
    print(f"Checking visibility of element located by {by} with value '{value}'...")

    def container_exists():
        return container and driver.execute_script(f"return document.querySelector('{container}') !== null;")

    def is_center_visible():
        script = f"""
        var element = {'document.evaluate("{value}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue' if by == By.XPATH else f'document.querySelector("{value}")'};
        if (element) {{
            var rect = element.getBoundingClientRect();
            var viewportHeight = window.innerHeight;
            return 0 <= rect.top + rect.height / 2 <= viewportHeight;
        }}
        return false;
        """
        return driver.execute_script(script)

    def is_at_bottom():
        return driver.execute_script("return (window.innerHeight + window.scrollY) >= document.body.scrollHeight;")

    def scroll_to_element():
        print("Starting scroll sequence to bring the element into view...")
        while not is_center_visible():
            if container_exists():
                print("Scrolling within the container...")
                driver.execute_script(f"document.querySelector('{container}').scrollBy(0, 100);")
            else:
                if is_at_bottom():
                    print("Reached the bottom of the page. Scrolling back up...")
                    human_like_scroll(driver, direction='up', total_scrolls=5)
                else:
                    print("Scrolling the page...")
                    human_like_scroll(driver, direction='down', total_scrolls=1)
            time.sleep(0.1)

    scroll_to_element()
    print("Element is now visible.")