import time
import random

def random_wait():
    """
    Waits for a random amount of time.
    - 95% chance: Wait between 2 and 5 seconds.
    - 5% chance: Wait between 30 minutes and 1 hour 45 minutes.
    """
    if random.random() < 0.001:  # 0.1% chance
        wait_time = random.randint(1800, 6300)  # 30 minutes (1800 seconds) to 1 hour 45 minutes (6300 seconds)
        print(f"Long random wait: {wait_time} seconds.")
    else:  # 95% chance
        wait_time = random.uniform(2, 7)  # 2 to 7 seconds
        print(f"Short random wait: {wait_time:.2f} seconds.")
    
    time.sleep(wait_time)


