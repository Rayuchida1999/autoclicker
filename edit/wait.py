import time
import random

class Wait:
    def __init__(self, min_seconds=1, max_seconds=5):
        self.min_seconds = min_seconds
        self.max_seconds = max_seconds

    def random_wait(self):
        # ランダムな秒数を生成して待機
        wait_time = random.uniform(self.min_seconds, self.max_seconds)
        time.sleep(wait_time)

# Waitクラスを使用してランダムな秒数待つ
wait = Wait(1, 3)
print(f"待機時間: {wait.min_seconds}～{wait.max_seconds} 秒の間でランダム")
wait.random_wait()

# 次の操作（例：クリック）など
print("クリック実行！")