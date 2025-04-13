from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
# Airワークを開く
driver.get("https://connect.airregi.jp/login?client_id=AWR&redirect_uri=https%3A%2F%2Fconnect.airregi.jp%2Foauth%2Fauthorize%3Fclient_id%3DAWR%26hruid%3D2f009358-2460-486f-a59f-c3ec491a1bc7%26nonce%3DtfbQmTvduwQQKI1yOBVseohmvkip5HxBW64myEUFPCo%26redirect_uri%3Dhttps%253A%252F%252Fats.rct.airwork.net%252Fairplf%252Flogin%252Fcb%26response_type%3Dcode%26scope%3Dopenid%2Bprofile%2Bemail%26state%3D41EzprGIYqt8wcvzn0nSWUo0ckENV3A2_ASkN_fkftM")
driver.implicitly_wait(10)

#ifs2021アカウントででグイン
account1 = driver.find_element(By.ID, 'account')
account1.send_keys('ifs2021')

password1 = driver.find_element(By.ID, 'password')
password1.send_keys('tukizi2024@')

login1 = driver.find_element(By.CLASS_NAME, 'primary')
login1.click()



WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
#ポチポチ準備
menu1 = driver.find_element(By.CLASS_NAME, 'styles_menuLink___TTEe')
menu1.click()
if menu1:
    print("menuクリックされました。")

driver.find_element(By.CSS_SELECTOR, ".styles_module__RPXUb[data-la-job-id='3587541'][aria-label='候補者を探す3587541']").click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
time.sleep(2)

#条件設定
conditions1 = driver.find_element(By.CSS_SELECTOR, "button[data-la='cadidate_conditions_modal_open_btn_click']")
conditions1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")


minGraduation1 = driver.find_element(By.NAME, "minimumFinalGraduationYear")
minGraduation1.send_keys(2010)
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
time.sleep(2)


collapse_btn1 = driver.find_element(By.CSS_SELECTOR, ".styles_collapse__Yl5mV[data-la='candidates_settings_detail_info_click_toggle']")
driver.execute_script("arguments[0].scrollIntoView();", collapse_btn1)
collapse_btn1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

if collapse_btn1:
    print("collapseクリックされました。")
time.sleep(2)

# 設定するを押す
detail_con1 = driver.find_element(By.XPATH, "//button[text()='設定する']")
driver.execute_script("arguments[0].scrollIntoView();", detail_con1)
detail_con1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
time.sleep(2)

if detail_con1:
    print("detailconクリックされました。")


# ITカテゴリの要素をクリック
it_category1 = driver.find_element(By.XPATH, "//div[@class='styles_rowTitle__Q0NNL' and text()='IT']")
driver.execute_script("arguments[0].scrollIntoView();", it_category1)
it_category1.click()
if it_category1 :
    print("ITカテゴリー押せました。")

programmer1 = driver.find_element(By.XPATH, "//span[text()='システムエンジニア']")
driver.execute_script("arguments[0].scrollIntoView();", programmer1)
programmer1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。１")
system_engineer1 = driver.find_element(By.XPATH, "//span[text()='プログラマー']")
driver.execute_script("arguments[0].scrollIntoView();", system_engineer1)
system_engineer1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。２")
project_management1 = driver.find_element(By.XPATH, "//span[text()='プロジェクト管理']")
driver.execute_script("arguments[0].scrollIntoView();", project_management1)
project_management1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。３")
product_manager1 = driver.find_element(By.XPATH, "//span[text()='プロダクトマネージャー']")
driver.execute_script("arguments[0].scrollIntoView();", product_manager1)
product_manager1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。４")
front_engineer1 = driver.find_element(By.XPATH, "//span[text()='フロントエンドエンジニア']")
driver.execute_script("arguments[0].scrollIntoView();", front_engineer1)
front_engineer1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。５")
server_engineer1 = driver.find_element(By.XPATH, "//span[contains(@id, ':r1v:') and text()='サーバーサイドエンジニア']")
driver.execute_script("arguments[0].scrollIntoView();", server_engineer1)
server_engineer1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。６")
database_engineer1 =  wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='データベースエンジニア']")))
driver.execute_script("arguments[0].scrollIntoView();", database_engineer1)
database_engineer1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。７")
network_engineer1 = driver.find_element(By.XPATH, "//span[text()='データベースエンジニア']")
driver.execute_script("arguments[0].scrollIntoView();", network_engineer1)
driver.execute_script("document.querySelector('h3').style.display='none';")
network_engineer1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。８")
security_engineer1 = driver.find_element(By.XPATH, "//span[text()='セキュリティエンジニア']")
driver.execute_script("arguments[0].scrollIntoView();", security_engineer1)
security_engineer1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。９")
data_engineer1 = driver.find_element(By.XPATH, "//span[text()='データエンジニア']")
driver.execute_script("arguments[0].scrollIntoView();", data_engineer1)
data_engineer1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。１０")

creative_design1 = driver.find_element(By.XPATH, "//div[@class='styles_rowTitle__Q0NNL' and text()='クリエイティブ/デザイン職']")
driver.execute_script("arguments[0].scrollIntoView();", creative_design1)
creative_design1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print('creativeクリックしました。')

web_service1 = driver.find_element(By.XPATH, "//span[text()='Webサービス/制作']")
driver.execute_script("arguments[0].scrollIntoView();", data_engineer1)
web_service1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。１１")
ad1 = driver.find_element(By.XPATH, "//span[text()='広告/グラフィック']")
driver.execute_script("arguments[0].scrollIntoView();", data_engineer1)
ad1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。１２")
game1 = driver.find_element(By.XPATH,"//span[text()='ゲーム']")
driver.execute_script("arguments[0].scrollIntoView();", data_engineer1)
game1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。１３")

#保存、検索
save1 = driver.find_element(By.XPATH, "//button[@class='styles_module__kr35h' and text()='保存する']")
driver.execute_script("arguments[0].scrollIntoView();", save1)
save1.click()

search1 = driver.find_element(By.XPATH, "//button[@class='styles_module__kr35h' and text()='検索する']")
driver.execute_script("arguments[0].scrollIntoView();", search1)
search1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
time.sleep(2)

#順序を変える
order_change1 = driver.find_element(By.XPATH, "//select[contains(@class, 'styles_module__EA2he') and contains(@class, 'styles_selectBox__tBbi2')]")
order_change1.click()
if order_change1:
    print('orderクリックしました')
    time.sleep(1)
order_select1 = driver.find_element(By.XPATH, "//option[text()='新着順']")
order_select1.click()
if order_select1:
    print('order選択しました。')

WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
time.sleep(2)

while True:
    WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
    candidates = driver.find_elements(By.CLASS_NAME, "styles_module__9b_0n")

    if not candidates:
        try:
            # 次ページがあれば押してループ続行
            next_button = driver.find_element(By.XPATH, "//a[contains(@class, 'styles_next__3LCdl')]")
            next_button.click()
            print('次のページに移動')

            WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
            time.sleep(3)  # 読み込み待ち

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
            driver.execute_script("arguments[0].scrollIntoView();", age_element)
            age_text = age_element.text.strip().replace("歳", "")
            
            # 年齢の値を検証
            if not age_text.isdigit():
                print(f"無効な年齢データ: '{age_text}' - スキップ")
                invalid_age_count += 1
                time.sleep(2)
                continue
            
            age = int(age_text)
            
            if age >= 35:
                # 「非表示」ボタンをクリック
                hide_button = candidate.find_element(By.XPATH, ".//button[text()='非表示']")
                hide_button.click()
                print('35歳以上のため非公開')
            else:
                # 「アプローチ」ボタンをクリック
                approach_button = candidate.find_element(By.XPATH, ".//button[text()='アプローチ']")
                approach_button.click()
                print('35歳以下のためアプローチ')

                # 「アプローチを送る」ボタンをクリック
                send_approach_button = driver.find_element(By.XPATH, "//button[text()='アプローチを送る']")
                send_approach_button.click()
            
            WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
            time.sleep(3)

        except Exception as e:
            print(f"エラー: {e}")
    
    # 無効な年齢データがすべての場合は次のページへ
    if invalid_age_count == len(candidates):
        try:
            next_button = driver.find_element(By.XPATH, "//a[contains(@class, 'styles_next__3LCdl')]")
            next_button.click()
            print("無効なデータのみのため次のページへ")
            WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
            time.sleep(3)
            continue
        except:
            print("次ページなし。処理終了")
            driver.quit()
            break

    WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
    time.sleep(2)  # ページ内処理待機


# ブラウザを閉じる
driver.quit()
print ('IFS終了')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>IFSからSystemSに移動


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Airワークを開く
driver.get("https://connect.airregi.jp/login?client_id=AWR&redirect_uri=https%3A%2F%2Fconnect.airregi.jp%2Foauth%2Fauthorize%3Fclient_id%3DAWR%26hruid%3D2f009358-2460-486f-a59f-c3ec491a1bc7%26nonce%3DtfbQmTvduwQQKI1yOBVseohmvkip5HxBW64myEUFPCo%26redirect_uri%3Dhttps%253A%252F%252Fats.rct.airwork.net%252Fairplf%252Flogin%252Fcb%26response_type%3Dcode%26scope%3Dopenid%2Bprofile%2Bemail%26state%3D41EzprGIYqt8wcvzn0nSWUo0ckENV3A2_ASkN_fkftM")
driver.implicitly_wait(10)

#ifs2021アカウントででグイン
account1 = driver.find_element(By.ID, 'account')
account1.send_keys('SystemS2024@')

password1 = driver.find_element(By.ID, 'password')
password1.send_keys('tukizi2024@')

login1 = driver.find_element(By.CLASS_NAME, 'primary')
login1.click()



WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
#ポチポチ準備
menu1 = driver.find_element(By.CLASS_NAME, 'styles_menuLink___TTEe')
menu1.click()
if menu1:
    print("menuクリックされました。")
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.styles_module__RPXUb[data-la-job-id='5272854'][aria-label='候補者を探す5272854']"))
).click()
time.sleep(2)

#条件設定
conditions1 = driver.find_element(By.CSS_SELECTOR, "button[data-la='cadidate_conditions_modal_open_btn_click']")
conditions1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

minGraduation1 = driver.find_element(By.NAME, "minimumFinalGraduationYear")
minGraduation1.send_keys(2010)
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
time.sleep(2)


collapse_btn1 = driver.find_element(By.CSS_SELECTOR, ".styles_collapse__Yl5mV[data-la='candidates_settings_detail_info_click_toggle']")
driver.execute_script("arguments[0].scrollIntoView();", collapse_btn1)
collapse_btn1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

if collapse_btn1:
    print("collapseクリックされました。")
time.sleep(2)

# 設定するを押す
detail_con1 = driver.find_element(By.XPATH, "//button[text()='設定する']")
driver.execute_script("arguments[0].scrollIntoView();", detail_con1)
detail_con1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
time.sleep(2)


if detail_con1:
    print("detailconクリックされました。")


# ITカテゴリの要素をクリック
it_category1 = driver.find_element(By.XPATH, "//div[@class='styles_rowTitle__Q0NNL' and text()='IT']")
driver.execute_script("arguments[0].scrollIntoView();", it_category1)
it_category1.click()
if it_category1 :
    print("ITカテゴリー押せました。")

programmer1 = driver.find_element(By.XPATH, "//span[text()='システムエンジニア']")
driver.execute_script("arguments[0].scrollIntoView();", programmer1)
programmer1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。１")
system_engineer1 = driver.find_element(By.XPATH, "//span[text()='プログラマー']")
driver.execute_script("arguments[0].scrollIntoView();", system_engineer1)
system_engineer1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。２")
project_management1 = driver.find_element(By.XPATH, "//span[text()='プロジェクト管理']")
driver.execute_script("arguments[0].scrollIntoView();", project_management1)
project_management1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。３")
product_manager1 = driver.find_element(By.XPATH, "//span[text()='プロダクトマネージャー']")
driver.execute_script("arguments[0].scrollIntoView();", product_manager1)
product_manager1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。４")
front_engineer1 = driver.find_element(By.XPATH, "//span[text()='フロントエンドエンジニア']")
driver.execute_script("arguments[0].scrollIntoView();", front_engineer1)
front_engineer1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。５")
server_engineer1 = driver.find_element(By.XPATH, "//span[contains(@id, ':r1v:') and text()='サーバーサイドエンジニア']")
driver.execute_script("arguments[0].scrollIntoView();", server_engineer1)
server_engineer1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。６")
database_engineer1 =  wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='データベースエンジニア']")))
driver.execute_script("arguments[0].scrollIntoView();", database_engineer1)
database_engineer1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。７")
network_engineer1 = driver.find_element(By.XPATH, "//span[text()='データベースエンジニア']")
driver.execute_script("arguments[0].scrollIntoView();", network_engineer1)
driver.execute_script("document.querySelector('h3').style.display='none';")
network_engineer1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。８")
security_engineer1 = driver.find_element(By.XPATH, "//span[text()='セキュリティエンジニア']")
driver.execute_script("arguments[0].scrollIntoView();", security_engineer1)
security_engineer1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。９")
data_engineer1 = driver.find_element(By.XPATH, "//span[text()='データエンジニア']")
driver.execute_script("arguments[0].scrollIntoView();", data_engineer1)
data_engineer1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。１０")

creative_design1 = driver.find_element(By.XPATH, "//div[@class='styles_rowTitle__Q0NNL' and text()='クリエイティブ/デザイン職']")
driver.execute_script("arguments[0].scrollIntoView();", creative_design1)
creative_design1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print('creativeクリックしました。')

web_service1 = driver.find_element(By.XPATH, "//span[text()='Webサービス/制作']")
driver.execute_script("arguments[0].scrollIntoView();", data_engineer1)
web_service1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。１１")
ad1 = driver.find_element(By.XPATH, "//span[text()='広告/グラフィック']")
driver.execute_script("arguments[0].scrollIntoView();", data_engineer1)
ad1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。１２")
game1 = driver.find_element(By.XPATH,"//span[text()='ゲーム']")
driver.execute_script("arguments[0].scrollIntoView();", data_engineer1)
game1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
print("クリックしました。１３")

#保存、検索
save1 = driver.find_element(By.XPATH, "//button[@class='styles_module__kr35h' and text()='保存する']")
driver.execute_script("arguments[0].scrollIntoView();", save1)
save1.click()

search1 = driver.find_element(By.XPATH, "//button[@class='styles_module__kr35h' and text()='検索する']")
driver.execute_script("arguments[0].scrollIntoView();", search1)
search1.click()
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
time.sleep(2)

#順序を変える
order_change1 = driver.find_element(By.XPATH, "//select[contains(@class, 'styles_module__EA2he') and contains(@class, 'styles_selectBox__tBbi2')]")
order_change1.click()
if order_change1:
    print('orderクリックしました')
    time.sleep(1)
order_select1 = driver.find_element(By.XPATH, "//option[text()='新着順']")
order_select1.click()
if order_select1:
    print('order選択しました。')

WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
time.sleep(2)

while True:
    WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
    candidates = driver.find_elements(By.CLASS_NAME, "styles_module__9b_0n")

    if not candidates:
        try:
            # 次ページがあれば押してループ続行
            next_button = driver.find_element(By.XPATH, "//a[contains(@class, 'styles_next__3LCdl')]")
            next_button.click()
            print('次のページに移動')

            WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
            time.sleep(3)  # 読み込み待ち

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
            driver.execute_script("arguments[0].scrollIntoView();", age_element)
            age_text = age_element.text.strip().replace("歳", "")
            
            # 年齢の値を検証
            if not age_text.isdigit():
                print(f"無効な年齢データ: '{age_text}' - スキップ")
                invalid_age_count += 1
                time.sleep(2)
                continue
            
            age = int(age_text)
            
            if age >= 35:
                # 「非表示」ボタンをクリック
                hide_button = candidate.find_element(By.XPATH, ".//button[text()='非表示']")
                hide_button.click()
                print('35歳以上のため非公開')
            else:
                # 「アプローチ」ボタンをクリック
                approach_button = candidate.find_element(By.XPATH, ".//button[text()='アプローチ']")
                approach_button.click()
                print('35歳以下のためアプローチ')

                # 「アプローチを送る」ボタンをクリック
                send_approach_button = driver.find_element(By.XPATH, "//button[text()='アプローチを送る']")
                send_approach_button.click()
            
            WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
            time.sleep(3)

        except Exception as e:
            print(f"エラー: {e}")
    
    # 無効な年齢データがすべての場合は次のページへ
    if invalid_age_count == len(candidates):
        try:
            next_button = driver.find_element(By.XPATH, "//a[contains(@class, 'styles_next__3LCdl')]")
            next_button.click()
            print("無効なデータのみのため次のページへ")
            WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
            time.sleep(3)
            continue
        except:
            print("次ページなし。処理終了")
            driver.quit()
            break

    WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
    time.sleep(2)  # ページ内処理待機


# ブラウザを閉じる
driver.quit()

print ('SystemS終了')
