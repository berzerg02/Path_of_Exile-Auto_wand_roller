import pyautogui
import mouseinfo
import mouse
import time
import pyauto


image_found = False
res = pyautogui.locateOnScreen('image.png', 1)
per10 = pyautogui.locateOnScreen('per10.png', 1)
list = ['per1.png', 'image.png']

while not image_found:
    res = pyautogui.locateCenterOnScreen(image=list[0], confidence=0.9, minSearchTime=0.5)
    if res is None:
        mouse.click('left')
    else:
        image_found = True

print(res)



