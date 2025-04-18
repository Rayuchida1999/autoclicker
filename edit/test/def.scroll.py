from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def detect_scroll_and_clicks(url, duration=15):
    """
    Opens the given URL, detects scroll distance every 0.1 seconds, and logs clicks on the page.

    :param url: The URL to open.
    :param duration: The duration (in seconds) to monitor scrolling and clicks.
    """
    # Initialize the WebDriver (ensure you have the appropriate driver installed)
    driver = webdriver.Chrome()  # Replace with your browser driver if needed
    driver.get(url)

    # Add a JavaScript event listener to detect clicks
    driver.execute_script(""" document.addEventListener('click', () => { console.log('クリックしました！'); }); """)

    start_time = time.time()
    last_scroll_position = driver.execute_script("return window.pageYOffset;")

    print("Monitoring scroll rate and clicks...")
    while time.time() - start_time < duration:
        current_scroll_position = driver.execute_script("return window.pageYOffset;")
        scroll_distance = current_scroll_position - last_scroll_position
        if scroll_distance > 0:
            direction = "downward"
        elif scroll_distance < 0:
            direction = "upward"
        else:
            direction = "no movement"
        print(f"Scroll distance: {abs(scroll_distance)}px in 0.05 sec ({direction})")
        last_scroll_position = current_scroll_position

        time.sleep(0.05)  # Check scroll position every 0.05 seconds

    print("Scroll and click monitoring completed.")
    driver.quit()

# Example usage
detect_scroll_and_clicks("https://rt-solutions.co.jp/")
