import pyautogui

screenWidth, screenHeight = pyautogui.size()

print screenHeight
print screenWidth

pyautogui.moveRel(-200, -200)
# pyautogui.moveTo(500, 500, duration=2)