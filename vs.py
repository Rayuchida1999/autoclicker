import pyautogui
import time
import random

# 8時間を秒に換算
total_time = 8 * 60 * 60  
interval = 15 * 60  # 15分ごと

start_time = time.time()  # 開始時間を記録

while time.time() - start_time < total_time:
    # 現在のマウス位置
    x, y = pyautogui.position()
    
    # ランダムな移動（10px以内）
    new_x = x + random.randint(-10, 10)
    new_y = y + random.randint(-10, 10)
    
    # カーソルを移動
    pyautogui.moveTo(new_x, new_y, duration=0.5)
    
    # 移動後の座標を表示
    print(f"Moved cursor from ({x}, {y}) to ({new_x}, {new_y})")
    
    # 15分待機
    time.sleep(interval)
