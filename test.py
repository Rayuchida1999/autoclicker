from edit.base import setup_driver
from edit.curser import Curser  # Import the Curser class
from edit.scroll import scroll_until_visible
from edit.wait import random_wait
from selenium.webdriver.common.by import By

# Initialize WebDriver
print("Initializing WebDriver...")
driver = setup_driver(headless=False)

# Initialize the Curser instance
curser = Curser(driver)

# Load the website
website = "file:///C:/Users/Ray Uchida/Desktop/autoclicker/edit/test/company.html"
driver.get(website)
print(f"WebDriver initialized and page loaded: {website}")

driver.implicitly_wait(10)

# Click "TOP" link using Curser
try:
    print("Clicking 'TOP' link...")
    top_element = driver.find_element(By.CSS_SELECTOR, "a[href='top.html']")
    curser(top_element)  # Use the Curser class to click the element
    print("Clicked 'TOP' link.")
except Exception as e:
    print(f"Error clicking 'TOP' link: {e}")

# Click "ブログ" link using Curser
try:
    print("Clicking 'ブログ' link...")
    blog_element = driver.find_element(By.CSS_SELECTOR, "a#blogLink")
    curser(blog_element)  # Use the Curser class to click the element
    print("Clicked 'ブログ' link.")
except Exception as e:
    print(f"Error clicking 'ブログ' link: {e}")

# Scroll to "お問い合わせ" link and click using Curser
try:
    print("Scrolling to 'お問い合わせ' link...")
    scroll_until_visible(driver, By.CSS_SELECTOR, "a[href='contact.html']")
    contact_element = driver.find_element(By.CSS_SELECTOR, "a[href='contact.html']")
    curser(contact_element)  # Use the Curser class to click the element
    print("Clicked 'お問い合わせ' link.")
except Exception as e:
    print(f"Error clicking 'お問い合わせ' link: {e}")

# Close the browser
print("Closing the browser...")
driver.quit()
print("Browser closed.")