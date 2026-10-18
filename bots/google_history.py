try:
    import pyautogui
    import time
except Exception:
    import os
    os.system('pip install pyautogui')
pyautogui.FAILSAFE = True

pyautogui.moveTo(1082, 1047, duration=0.1)
pyautogui.click()
for i in range(20):
    pyautogui.moveTo(1053, 89, duration=0.1)
    pyautogui.click()
    pyautogui.write('youtube.com')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.moveTo(436, 30, duration=0.1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(385, 34, duration=0.1)
    pyautogui.click()
    pyautogui.moveTo(1053, 89, duration=0.1)
    pyautogui.click()