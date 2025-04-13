import time
import random
from selenium.common.exceptions import NoSuchElementException

# --- スクロール関数 ---
def human_like_scroll(driver, total_distance=1000):
    steps = random.randint(15, 30)  # スクロール回数を乱数で設定
    scrolled = 0
    scroll_deltas = []

    # 最初は速く、だんだん遅くスクロールするためのデルタを生成
    for i in range(steps):
        factor = (1 - (i / steps)) ** 2  # 減速感を出す
        delta = int(total_distance * factor / steps)
        scroll_deltas.append(delta)

    for delta in scroll_deltas:
        scrolled += delta
        driver.execute_script(f"window.scrollBy(0, {delta});")  # 少しずつスクロール
        sleep_time = random.uniform(0.1, 0.3)  # スリープ時間を増やしてゆっくりスクロール
        time.sleep(sleep_time)

    print(f"Total scrolled: {scrolled} px")

def scroll_down(driver, until_element=None, by=None, value=None):
    """
    Scrolls down the page. If `until_element` is provided, scrolls until the element is visible.
    
    :param driver: WebDriver instance
    :param until_element: Boolean flag to scroll until an element is visible
    :param by: Locator strategy (e.g., By.ID, By.XPATH)
    :param value: Locator value
    """
    if until_element and by and value:
        while True:
            try:
                element = driver.find_element(by, value)
                if element.is_displayed():
                    break
            except NoSuchElementException:
                pass
            driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(0.5)
    else:
        # Default behavior: scroll to the bottom of the page
        scroll_height = driver.execute_script("return document.body.scrollHeight")
        current_position = 0
        step = 100  # Scroll step size

        while current_position < scroll_height:
            driver.execute_script(f"window.scrollBy(0, {step});")
            current_position += step
            time.sleep(0.2)

def scroll_until_visible(driver, by, value):
    # 要素が見つかるまでスクロール
    while True:
        try:
            element = driver.find_element(by, value)
            if element.is_displayed():
                break
        except NoSuchElementException:
            pass
        driver.execute_script("window.scrollBy(0, 300);")  # 少しずつスクロール
        time.sleep(0.5)  # スリープ時間を追加してゆっくりスクロール
    driver.execute_script("window.scrollBy(0, 600);")  # 見つかった後さらに少しスクロール

# --- 使用例 ---
# driver = webdriver.Chrome(...)  # WebDriver のセットアップ
# human_like_scroll(driver, total_distance=1200)