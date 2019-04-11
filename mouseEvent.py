import pyautogui 
import random
def mouseMove(tl,tw,th,sizes):
# t1数组 t1[0]匹配位置的X t1[0]匹配位置的Y tw用于匹配图片的宽 th用于匹配图片的高
    pyautogui.moveTo(tl[0]+random.randint(tw*(0+sizes),tw*(1+sizes)),tl[1]+random.randint(0,th))
# 鼠标点击事件
def mouseClick():
    pyautogui.doubleClick(duration=0.25)