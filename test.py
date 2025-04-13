from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from edit.wait import Wait
from edit.scroll import scroll_down, scroll_until_visible

# --- WebDriver 起動 ---
# 指定された URL にアクセス
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rt-solutions.co.jp/")

driver.implicitly_wait(10)

# Wait クラスのインスタンスを作成
wait = Wait()

# <a href="https://rt-solutions.co.jp/company">会社概要</a> をクリック
wait.random_wait()
try:
    company_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "会社概要"))
    )
except:
    # If "会社概要" is not found, click the menu button first
    menu_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "header__hMenu"))
    )
    menu_button.click()
    wait.random_wait()  # Wait for the menu to expand
    company_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "会社概要"))
    )

company_link.click()

# ページの一番下までスクロール
scroll_down(driver)

# 再度ランダムな時間待機
wait.random_wait()

# <a href="https://rt-solutions.co.jp/contact">お問い合わせ</a> をクリック
try:
    click1 = driver.find_element(By.LINK_TEXT, "お問い合わせ")
except:
    # If "お問い合わせ" is not found, click the menu button first
    menu_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "header__hMenu"))
    )
    menu_button.click()
    wait.random_wait()  # Wait for the menu to expand
    click1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "お問い合わせ"))
    )

# Scroll until the "お問い合わせ" link is visible
scroll_down(driver, until_element=True, by=By.LINK_TEXT, value="お問い合わせ")

click1.click()

# <textarea> をクリック
wait.random_wait()

# Scroll until the <textarea> element is visible
scroll_until_visible(driver, by=By.XPATH, value="//textarea[@name='お問い合わせ内容']")

click2 = driver.find_element(By.XPATH, "//textarea[@name='お問い合わせ内容']")
click2.click()

# テキストを入力
wait.random_wait()
type_area = driver.find_element(By.XPATH, "//textarea[@name='お問い合わせ内容']")
type_area.send_keys("テストメッセージ")

# 最後の待機
wait.random_wait()

# 必要に応じて、ページ遷移後の処理を記述
print("コード終了")


# ブラウザを閉じる
driver.quit()