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

class Typing:
    def __init__(self, driver):
        """
        Initialize the Typing class with a Selenium WebDriver instance.
        :param driver: Selenium WebDriver instance
        """
        self.driver = driver

    def __call__(self, type_area, text, language="en"):
        """
        Allow the Typing instance to be called directly with an element, text, and language.
        :param type_area: The input element where text will be typed.
        :param text: The text to type.
        :param language: The language of the text ("en" for English, "jp" for Japanese).
        """
        self.human_like_typing(type_area, text, language)

    def human_like_typing(self, type_area, text, language="en"):
        """
        Simulates human-like typing behavior, including mistakes and corrections.

        :param type_area: The input element where text will be typed.
        :param text: The text to type.
        :param language: The language of the text ("en" for English, "jp" for Japanese).
        """
        # Focus the element using JavaScript to avoid click interception
        print("Focusing the input field using JavaScript...")
        driver = type_area.parent  # Get the WebDriver instance from the element
        driver.execute_script("arguments[0].focus();", type_area)

        romaji_to_hiragana = {
            "a": "あ", "i": "い", "u": "う", "e": "え", "o": "お",
            "ka": "か", "ki": "き", "ku": "く", "ke": "け", "ko": "こ",
            "sa": "さ", "shi": "し", "su": "す", "se": "せ", "so": "そ",
            "ta": "た", "chi": "ち", "tsu": "つ", "te": "て", "to": "と",
            "na": "な", "ni": "に", "nu": "ぬ", "ne": "ね", "no": "の",
            "ha": "は", "hi": "ひ", "fu": "ふ", "he": "へ", "ho": "ほ",
            "ma": "ま", "mi": "み", "mu": "む", "me": "め", "mo": "も",
            "ya": "や", "yu": "ゆ", "yo": "よ",
            "ra": "ら", "ri": "り", "ru": "る", "re": "れ", "ro": "ろ",
            "wa": "わ", "wo": "を", "n": "ん"
        }

        if language == "jp":
            buffer = ""  # Buffer to hold romaji input
            for char in text:
                buffer += char.lower()  # Ensure lowercase for matching
                print(f"Buffer: {buffer}")
                if buffer in romaji_to_hiragana:
                    hiragana = romaji_to_hiragana[buffer]
                    print(f"Typing hiragana: {hiragana}")
                    type_area.send_keys(hiragana)  # Type the converted hiragana
                    print("Sleeping...")
                    time.sleep(random.uniform(0.01, 0.15))  # Adjusted pause for 35 wpm
                    buffer = ""  # Clear the buffer after conversion
                elif len(buffer) > 2:  # If buffer doesn't match, reset it
                    print(f"Typing unmatched buffer: {buffer[0]}")
                    type_area.send_keys(buffer[0])  # Type the first character
                    buffer = buffer[1:]  # Shift the buffer
            if buffer:  # Type any remaining characters in the buffer
                print(f"Typing remaining buffer: {buffer}")
                type_area.send_keys(buffer)
        else:
            typed_text = ""
            for char in text:
                # Simulate typing speed (35 wpm = ~170ms to 200ms per character)
                print(f"Typing character: {char}")
                print("Sleeping...")
                time.sleep(random.uniform(0.01, 0.15))  # Adjusted pause for 35 wpm

                # Introduce occasional typing mistakes
                if random.random() < 0.05:  # 10% chance of making a mistake
                    mistake_char = random.choice(KEYBOARD_NEIGHBORS.get(char.lower(), [char]))
                    print(f"Typing mistake: {mistake_char}")
                    type_area.send_keys(mistake_char)  # Type the wrong character
                    print("Sleeping before correcting...")
                    time.sleep(random.uniform(0.4, 1))  # Pause before correcting
                    type_area.send_keys("\b")  # Backspace to correct the mistake

                # Type the correct character
                type_area.send_keys(char)
                typed_text += char

                # Log the current state of typing
                print(f"Typed so far: {typed_text}")

        print("Typing completed.")
