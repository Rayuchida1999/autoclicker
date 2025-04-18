from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_driver(headless=False):
    """
    Sets up the WebDriver with anti-detection measures.
    :param headless: Whether to run the browser in headless mode.
    :return: Configured WebDriver instance.
    """
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.77 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    # Anti-detection measures
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
        Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5] });
        Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
        Object.defineProperty(navigator, 'platform', { get: () => 'Win32' });
        """
    })

    print("WebDriver setup complete with anti-detection measures.")
    return driver

class CursorManager:
    def __init__(self, driver):
        """
        Initialize the CursorManager with a Selenium WebDriver instance.
        :param driver: Selenium WebDriver instance
        """
        self.driver = driver

    def initialize_cursor(self):
        """
        Inject custom cursor HTML, CSS, and JavaScript into the page to display the cursor.
        """
        try:
            cursor_html = """
            if (!document.getElementById('customCursor')) {
                const style = document.createElement('style');
                style.textContent = `
                    body {
                        cursor: none; /* Hide the default cursor */
                    }
                    #customCursor {
                        position: absolute;
                        pointer-events: none;
                        z-index: 10000;
                        width: 75px;
                        height: 75px;
                    }
                    #customCursor svg polygon {
                        stroke-linejoin: bevel;
                    }
                `;
                document.head.appendChild(style);

                const cursor = document.createElement('div');
                cursor.id = 'customCursor';
                cursor.innerHTML = `
                    <svg width="75" height="75" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
                        <polygon points="25,8 24.5,41 31.5,33 37,44 43,40.5 37.5,31 47,31" 
                                 fill="white" stroke="black" stroke-width="1.5"/>
                    </svg>
                `;
                document.body.appendChild(cursor);

                document.addEventListener('mousemove', (e) => {
                    cursor.style.left = `${e.clientX}px`;
                    cursor.style.top = `${e.clientY}px`;
                });
            }
            """
            self.driver.execute_script(cursor_html)
            print("✅ Custom cursor initialized.")
        except Exception as e:
            print(f"Error in initialize_cursor: {e}")

    def set_text_cursor(self):
        """
        Change the cursor to the text cursor.
        """
        try:
            self.driver.execute_script("""
            const cursor = document.getElementById('customCursor');
            if (cursor) {
                cursor.innerHTML = `
                    <svg width="75" height="75" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
                        <polygon points="26,8 30,8" fill="white" stroke="black" stroke-width="1"/>
                        <polygon points="30.5,8.5 30.5,25" fill="white" stroke="black" stroke-width="1"/>
                        <polygon points="26,25.5 30,25.5" fill="white" stroke="black" stroke-width="1"/>
                        <polygon points="31,8 35,8" fill="white" stroke="black" stroke-width="1"/>
                        <polygon points="31,25.5 35,25.5" fill="white" stroke="black" stroke-width="1"/>
                    </svg>
                `;
            }
            """)
            print("✅ Cursor changed to text cursor.")
        except Exception as e:
            print(f"Error in set_text_cursor: {e}")

    def reset_cursor(self):
        """
        Reset the cursor to the default SVG cursor.
        """
        try:
            self.initialize_cursor()
        except Exception as e:
            print(f"Error in reset_cursor: {e}")

