import pyautogui
import time
import turtle as t
pyautogui.FAILSAFE = True

pyautogui.moveTo(1082, 1047, 0.1)
pyautogui.click()
pyautogui.moveTo(72, 853, duration=0.1)
pyautogui.click()
pyautogui.click()
time.sleep(19.5)
pyautogui.moveTo(1136, 805, duration=0.1)
pyautogui.click()
time.sleep(36.6)
pyautogui.moveTo(985, 481, duration=0.1)
pyautogui.click()
t.pencolor('green')
t.bgcolor('black')
t.pensize(5)
t.forward(200)
t.home()
t.backward(200)
t.home()
t.write('Done!', font=('Arial', 30, 'bold'))
t.done()