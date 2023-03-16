import pyautogui as pg
import time

# time.sleep(5)
pg.leftClick(1218,1078,1,2)
pg.typewrite("https://www.youtube.com/")
pg.press("enter")
# print(pg.position())
time.sleep(2)
pg.click(1046,164)
pg.typewrite("triggered insaan")
pg.press("enter")
pg.screenshot("hello.jpg")