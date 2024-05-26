import pyautogui
import time
def press_key_multiple_times(key, times, interval=0.1):
    for _ in range(times):
        pyautogui.press(key)
        time.sleep(interval)

def go_to_gym():
    pyautogui.press('z')


go_to_gym()