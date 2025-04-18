from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from edit.scroll import scroll_until_visible  # Import scroll_modal_until_visible function
from edit.wait import random_wait  # Import random_wait function
from edit.type import human_like_typing  # Import human_like_typing function
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Airワークを開く
driver.get("https://connect.airregi.jp/login?client_id=AWR&redirect_uri=https%3A%2F%2Fconnect.airregi.jp%2Foauth%2Fauthorize%3Fclient_id%3DAWR%26hruid%3D2f009358-2460-486f-a59f-c3ec491a1bc7%26nonce%3DtfbQmTvduwQQKI1yOBVseohmvkip5HxBW64myEUFPCo%26redirect_uri%3Dhttps%253A%252F%252Fats.rct.airwork.net%252Fairplf%252Flogin%252Fcb%26response_type%3Dcode%26scope%3Dopenid%2Bprofile%2Bemail%26state%3D41EzprGIYqt8wcvzn0nSWUo0ckENV3A2_ASkN_fkftM")
driver.implicitly_wait(10)

# ifs2021アカウントでログイン
account1 = driver.find_element(By.ID, 'account')
human_like_typing(account1, 'ifs2021')  # Use human_like_typing for typing
random_wait()  # Add random_wait after typing

password1 = driver.find_element(By.ID, 'password')
human_like_typing(password1, 'tukizi2024@')  # Use human_like_typing for typing
random_wait()  # Add random_wait after typing

login1 = driver.find_element(By.CLASS_NAME, 'primary')
login1.click()
random_wait()  # Add random_wait after clicking

WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

# ポチポチ準備
element = driver.find_element(By.CLASS_NAME, 'styles_menuLink___TTEe')
element.click()  # Directly click the element
print("menuクリックされました。")
random_wait()  # Use random_wait

scroll_until_visible(driver, By.CSS_SELECTOR, ".styles_module__RPXUb[data-la-job-id='3587541'][aria-label='候補者を探す3587541']", click=True)
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
random_wait()

# 条件設定
scroll_until_visible(driver, By.CSS_SELECTOR, "button[data-la='cadidate_conditions_modal_open_btn_click']", click=True)
random_wait()  # Add random_wait after clicking
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
# 条件設定 (inside modal)
modal_selector = ".modal-open"  # Specify the modal's selector

minGraduation1 = scroll_modal_until_visible(driver, modal_selector, By.NAME, "minimumFinalGraduationYear", click=False)  # Get the element without clicking
if minGraduation1:
    human_like_typing(minGraduation1, "2010")  # Use human_like_typing for typing
    random_wait()  # Add random_wait after typing
else:
    print("Failed to locate the 'minimumFinalGraduationYear' input field.")

scroll_modal_until_visible(driver, modal_selector, By.CSS_SELECTOR, ".styles_collapse__Yl5mV[data-la='candidates_settings_detail_info_click_toggle']", click=True)
random_wait()  # Add random_wait after clicking
print("collapseクリックされました。")
random_wait()

# 設定するを押す
scroll_modal_until_visible(driver, modal_selector, By.XPATH, "//button[text()='設定する']", click=True)
random_wait()  # Add random_wait after clicking
print("detailconクリックされました。")

# ITカテゴリの要素をクリック (inside modal)
modal_selector = ".styles_form__LdvVl"  # Specify the modal's selector

scroll_modal_until_visible(driver, modal_selector, By.XPATH, "//div[@class='styles_rowTitle__Q0NNL' and text()='IT']", click=True)
print("ITカテゴリー押せました。")
random_wait()  # Add random_wait after clicking

# Example: Click multiple elements inside the modal
categories = [
    "//span[text()='システムエンジニア']",
    "//span[text()='プログラマー']",
    "//span[text()='プロジェクト管理']",
    "//span[text()='プロダクトマネージャー']",
    "//span[text()='フロントエンドエンジニア']",
    "//span[contains(@id, ':r1v:') and text()='サーバーサイドエンジニア']",
    "//span[text()='データベースエンジニア']",
    "//span[text()='セキュリティエンジニア']",
    "//span[text()='データエンジニア']"
]

for category in categories:
    scroll_modal_until_visible(driver, modal_selector, By.XPATH, category, click=True)
    random_wait()  # Add random_wait between each category
    print(f"クリックしました: {category}")

# 保存、検索 (inside modal)
scroll_modal_until_visible(driver, modal_selector, By.XPATH, "//button[@class='styles_module__kr35h' and text()='保存する']", click=True)
random_wait()  # Add random_wait after clicking
scroll_until_visible(driver, By.XPATH, "//button[@class='styles_module__kr35h' and text()='検索する']", click=True)
random_wait()  # Add random_wait after clicking
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
random_wait()

# 順序を変える
scroll_until_visible(driver, By.XPATH, "//select[contains(@class, 'styles_module__EA2he') and contains(@class, 'styles_selectBox__tBbi2')]", click=True)
random_wait()  # Add random_wait after clicking
scroll_until_visible(driver, By.XPATH, "//option[text()='新着順']", click=True)
random_wait()  # Add random_wait after clicking
print('order選択しました。')

while True:
    WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
    candidates = driver.find_elements(By.CLASS_NAME, "styles_module__9b_0n")

    if not candidates:
        try:
            # 次ページがあれば押してループ続行
            scroll_until_visible(driver, By.XPATH, "//a[contains(@class, 'styles_next__3LCdl')]", click=True)
            random_wait()  # Add random_wait after clicking
            print('次のページに移動')

            WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
            random_wait()  # Use random_wait

            # 次のページで年齢要素が存在するかチェック
            first_age_elements = driver.find_elements(By.XPATH, ".//p[1]")
            if not first_age_elements:
                print("年齢要素が見つからないため終了")
                driver.quit()
                break

            continue
        except:
            print("次ページなし。処理終了")
            driver.quit()
            break  # すべてのページ処理完了

    invalid_age_count = 0
    
    for candidate in candidates:
        try:
            # 年齢を取得
            age_element = candidate.find_element(By.XPATH, ".//p[1]")
            scroll_until_visible(driver, By.XPATH, ".//p[1]")  # Use scroll_until_visible
            random_wait()  # Add random_wait after scrolling
            age_text = age_element.text.strip().replace("歳", "")
            
            # 年齢の値を検証
            if not age_text.isdigit():
                print(f"無効な年齢データ: '{age_text}' - スキップ")
                invalid_age_count += 1
                random_wait()  # Add random_wait
                continue
            
            age = int(age_text)
            
            if age >= 35:
                # 「非表示」ボタンをクリック
                scroll_until_visible(candidate, By.XPATH, ".//button[text()='非表示']", click=True)
                random_wait()  # Add random_wait after clicking
                print('35歳以上のため非公開')
            else:
                # 「アプローチ」ボタンをクリック
                scroll_until_visible(candidate, By.XPATH, ".//button[text()='アプローチ']", click=True)
                random_wait()  # Add random_wait after clicking
                print('35歳以下のためアプローチ')

                # 「アプローチを送る」ボタンをクリック
                scroll_until_visible(driver, By.XPATH, "//button[text()='アプローチを送る']", click=True)
                random_wait()  # Add random_wait after clicking
            
            WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
            random_wait()  # Use random_wait

        except Exception as e:
            print(f"エラー: {e}")
    
    # 無効な年齢データがすべての場合は次のページへ
    if invalid_age_count == len(candidates):
        try:
            scroll_until_visible(driver, By.XPATH, "//a[contains(@class, 'styles_next__3LCdl')]", click=True)
            random_wait()  # Add random_wait after clicking
            print("無効なデータのみのため次のページへ")
            WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
            random_wait()  # Use random_wait
            continue
        except:
            print("次ページなし。処理終了")
            driver.quit()
            break

    WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
    random_wait()  # ページ内処理待機

# ブラウザを閉じる
driver.quit()
print('IFS終了')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>IFSからSystemSに移動

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Airワークを開く
driver.get("https://connect.airregi.jp/login?client_id=AWR&redirect_uri=https%3A%2F%2Fconnect.airregi.jp%2Foauth%2Fauthorize%3Fclient_id%3DAWR%26hruid%3D2f009358-2460-486f-a59f-c3ec491a1bc7%26nonce%3DtfbQmTvduwQQKI1yOBVseohmvkip5HxBW64myEUFPCo%26redirect_uri%3Dhttps%253A%252F%252Fats.rct.airwork.net%252Fairplf%252Flogin%252Fcb%26response_type%3Dcode%26scope%3Dopenid%2Bprofile%2Bemail%26state%3D41EzprGIYqt8wcvzn0nSWUo0ckENV3A2_ASkN_fkftM")
driver.implicitly_wait(10)

# ifs2021アカウントでログイン
account1 = driver.find_element(By.ID, 'account')
human_like_typing(account1, 'SystemS2024@')  # Use human_like_typing for typing
random_wait()  # Add random_wait after typing

password1 = driver.find_element(By.ID, 'password')
human_like_typing(password1, 'tukizi2024@')  # Use human_like_typing for typing
random_wait()  # Add random_wait after typing

login1 = driver.find_element(By.CLASS_NAME, 'primary')
login1.click()
random_wait()  # Add random_wait after clicking

WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

# ポチポチ準備
random_wait()  # Use random_wait
scroll_until_visible(driver, By.CLASS_NAME, 'styles_menuLink___TTEe', click=True)  # Use scroll_until_visible
random_wait()  # Add random_wait after clicking
print("menuクリックされました。")

random_wait()  # Use random_wait
scroll_until_visible(driver, By.CSS_SELECTOR, "a.styles_module__RPXUb[data-la-job-id='5272854'][aria-label='候補者を探す5272854']", click=True)
random_wait()  # Add random_wait after clicking

# 条件設定 (inside modal)
modal_selector1 = ".modal-open"  # Specify the modal's selector

minGraduation1 = scroll_modal_until_visible(driver, modal_selector1, By.NAME, "minimumFinalGraduationYear", click=False)  # Get the element without clicking
if minGraduation1:
    human_like_typing(minGraduation1, "2010")  # Use human_like_typing for typing
    random_wait()  # Add random_wait after typing
else:
    print("Failed to locate the 'minimumFinalGraduationYear' input field.")

scroll_modal_until_visible(driver, modal_selector1, By.CSS_SELECTOR, ".styles_collapse__Yl5mV[data-la='candidates_settings_detail_info_click_toggle']", click=True)
random_wait()  # Add random_wait after clicking
print("collapseクリックされました。")
random_wait()

# 設定するを押す
scroll_modal_until_visible(driver, modal_selector1, By.XPATH, "//button[text()='設定する']", click=True)
random_wait()  # Add random_wait after clicking
print("detailconクリックされました。")

# ITカテゴリの要素をクリック (inside modal)
modal_selector2 = ".styles_form__LdvVl"  # Specify the modal's selector

scroll_modal_until_visible(driver, modal_selector2, By.XPATH, "//div[@class='styles_rowTitle__Q0NNL' and text()='IT']", click=True)
random_wait()  # Add random_wait after clicking
print("ITカテゴリー押せました。")

# Example: Click multiple elements inside the modal
categories = [
    "//span[text()='システムエンジニア']",
    "//span[text()='プログラマー']",
    "//span[text()='プロジェクト管理']",
    "//span[text()='プロダクトマネージャー']",
    "//span[text()='フロントエンドエンジニア']",
    "//span[contains(@id, ':r1v:') and text()='サーバーサイドエンジニア']",
    "//span[text()='データベースエンジニア']",
    "//span[text()='セキュリティエンジニア']",
    "//span[text()='データエンジニア']"
]

for category in categories:
    scroll_modal_until_visible(driver, modal_selector2, By.XPATH, category, click=True)
    random_wait()  # Add random_wait between each category
    print(f"クリックしました: {category}")

# 保存、検索 (inside modal)
scroll_modal_until_visible(driver, modal_selector2, By.XPATH, "//button[@class='styles_module__kr35h' and text()='保存する']", click=True)
random_wait()  # Add random_wait after clicking
scroll_until_visible(driver, By.XPATH, "//button[@class='styles_module__kr35h' and text()='検索する']", click=True)
random_wait()  # Add random_wait after clicking
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
random_wait()

# 順序を変える
scroll_until_visible(driver, By.XPATH, "//select[contains(@class, 'styles_module__EA2he') and contains(@class, 'styles_selectBox__tBbi2')]", click=True)
random_wait()  # Add random_wait after clicking
scroll_until_visible(driver, By.XPATH, "//option[text()='新着順']", click=True)
random_wait()  # Add random_wait after clicking
print('order選択しました。')

while True:
    WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
    candidates = driver.find_elements(By.CLASS_NAME, "styles_module__9b_0n")

    if not candidates:
        try:
            # 次ページがあれば押してループ続行
            scroll_until_visible(driver, By.XPATH, "//a[contains(@class, 'styles_next__3LCdl')]", click=True)
            random_wait()  # Add random_wait after clicking
            print('次のページに移動')

            WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
            random_wait()  # Use random_wait

            # 次のページで年齢要素が存在するかチェック
            first_age_elements = driver.find_elements(By.XPATH, ".//p[1]")
            if not first_age_elements:
                print("年齢要素が見つからないため終了")
                driver.quit()
                break

            continue
        except:
            print("次ページなし。処理終了")
            driver.quit()
            break  # すべてのページ処理完了

    invalid_age_count = 0
    
    for candidate in candidates:
        try:
            # 年齢を取得
            age_element = candidate.find_element(By.XPATH, ".//p[1]")
            scroll_until_visible(driver, By.XPATH, ".//p[1]")  # Use scroll_until_visible
            random_wait()  # Add random_wait after scrolling
            age_text = age_element.text.strip().replace("歳", "")
            
            # 年齢の値を検証
            if not age_text.isdigit():
                print(f"無効な年齢データ: '{age_text}' - スキップ")
                invalid_age_count += 1
                random_wait()  # Add random_wait
                continue
            
            age = int(age_text)
            
            if age >= 35:
                # 「非表示」ボタンをクリック
                scroll_until_visible(candidate, By.XPATH, ".//button[text()='非表示']", click=True)
                random_wait()  # Add random_wait after clicking
                print('35歳以上のため非公開')
            else:
                # 「アプローチ」ボタンをクリック
                scroll_until_visible(candidate, By.XPATH, ".//button[text()='アプローチ']", click=True)
                random_wait()  # Add random_wait after clicking
                print('35歳以下のためアプローチ')

                # 「アプローチを送る」ボタンをクリック
                scroll_until_visible(driver, By.XPATH, "//button[text()='アプローチを送る']", click=True)
                random_wait()  # Add random_wait after clicking
            
            WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
            random_wait()  # Use random_wait

        except Exception as e:
            print(f"エラー: {e}")
    
    # 無効な年齢データがすべての場合は次のページへ
    if invalid_age_count == len(candidates):
        try:
            scroll_until_visible(driver, By.XPATH, "//a[contains(@class, 'styles_next__3LCdl')]", click=True)
            random_wait()  # Add random_wait after clicking
            print("無効なデータのみのため次のページへ")
            WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
            random_wait()  # Use random_wait
            continue
        except:
            print("次ページなし。処理終了")
            driver.quit()
            break

    WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
    random_wait()  # ページ内処理待機

# ブラウザを閉じる
driver.quit()
print('SystemS終了')
