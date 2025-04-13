import time
import random

# キーボードの近いキーを定義 (例: QWERTY 配列)
KEYBOARD_NEIGHBORS = {
    "a": ["q", "s", "z"],
    "b": ["v", "n", "g"],
    "c": ["x", "v", "d"],
    "d": ["s", "f", "e"],
    "e": ["w", "r", "d"],
    "f": ["d", "g", "r"],
    "g": ["f", "h", "t"],
    "h": ["g", "j", "y"],
    "i": ["u", "o", "k"],
    "k": ["j", "l", "i"],
    "l": ["k", "o", "p"],
    "m": ["n", "j", "k"],
    "n": ["b", "m", "h"],
    "o": ["i", "p", "l"],
    "p": ["o", "l", ";"],
    "q": ["w", "a", "s"],
    "r": ["e", "t", "f"],
    "s": ["a", "d", "w"],
    "t": ["r", "y", "g"],
    "u": ["y", "i", "j"],
    "v": ["c", "b", "f"],
    "w": ["q", "e", "s"],
    "x": ["z", "c", "d"],
    "y": ["t", "u", "h"],
    "z": ["x", "a", "s"],
    " ": [" "],  # スペースキー
}

def human_like_typing(type_area, text, language="en"):
    """
    Simulates human-like typing behavior, including mistakes and corrections.

    :param type_area: The input element where text will be typed.
    :param text: The text to type.
    :param language: The language of the text ("en" for English, "jp" for Japanese).
    """
    typed_text = ""
    for char in text:
        # Simulate typing speed (40 wpm = ~150ms per character)
        time.sleep(random.uniform(0.1, 0.2))

        # Introduce occasional typing mistakes
        if random.random() < 0.1:  # 10% chance of making a mistake
            mistake_char = random.choice(KEYBOARD_NEIGHBORS.get(char.lower(), [char]))
            type_area.send_keys(mistake_char)
            time.sleep(random.uniform(0.1, 0.2))  # Pause before correcting
            type_area.send_keys("\b")  # Backspace to correct the mistake

        # Type the correct character
        type_area.send_keys(char)
        typed_text += char

        # Log the current state of typing
        print(f"Typed so far: {typed_text}")

        # Handle Japanese input (simulate IME behavior)
        if language == "jp" and char in "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん":
            time.sleep(random.uniform(0.2, 0.4))  # Pause for IME conversion
            type_area.send_keys("\n")  # Simulate pressing Enter for IME conversion

    print("Typing completed.")
