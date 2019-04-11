import cv2 as cv
import numpy as np
import random
import win32gui, win32con, win32api
import time
import configData

def template_image(targetImg,tplImg):
    target = cv.imread(targetImg)
    tpl = cv.imread(tplImg)
    methods = [cv.TM_SQDIFF_NORMED]
    configData.th, configData.tw = tpl.shape[:2]
    
    for md in methods:
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        
        if md == cv.TM_SQDIFF_NORMED:
            configData.tl = min_loc
        else:
            configData.tl = max_loc
        if(min_val==1.0 or min_val>0.12 or min_val>1):
            return False
        return True


