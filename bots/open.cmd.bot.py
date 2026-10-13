
import pyautogui
import time
pyautogui.FAILSAFE = True
x , y = pyautogui.position()
print(x, y)

pyautogui.moveTo(1083, 1044, duration=0.1)

pyautogui.click()


pyautogui.moveTo(356, 1050, duration=0.1)
pyautogui.click()
pyautogui.write('cmd')
pyautogui.press('enter')
time.sleep(0.5)

pyautogui.moveTo(581, 229, duration=0.1)
pyautogui.click()
pyautogui.write('color a')
pyautogui.press('enter')
pyautogui.write('dir /s')
pyautogui.press('enter')
