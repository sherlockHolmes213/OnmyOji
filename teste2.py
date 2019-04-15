import cv2 as cv
import numpy as np
import configData
import random
import sys
import ctypes
def template_demo():
    target= cv.imread("b.png")
    tpl = cv.imread("images/account.png")
    # tpl = cv.imread("images/sure.png")
    # cv.imshow("template image",tpl)
    # cv.imshow("target image",target)
    # methods = [cv.TM_SQDIFF_NORMED,cv.TM_SQDIFF,cv.TM_CCORR,cv.TM_CCORR_NORMED,cv.TM_CCOEFF,cv.TM_CCOEFF_NORMED]
    methods = [cv.TM_SQDIFF_NORMED]
    th,tw = tpl.shape[:2]
    for md in methods:
        result = cv.matchTemplate(target,tpl,md)
        min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)
        print(min_val,max_val)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        # br = (tl[0]+tw,tl[1]+th)
        br = (tl[0]+random.randint(0,tw*1),tl[1]+random.randint(0,th))
        cv.rectangle(target,tl,br,(0,0,255),2)
        cv.imshow("match-%s"%md,target)


template_demo()
cv.waitKey(0)
cv.destroyAllWindows()
# print("正在刷 %s ,已经进行 %d 次"%(configData.wareConfigData["wareName"][configData.wareType],configData.count))
# print(configData.wareConfigData["wareName"][configData.wareType])
# print(configData.count)

# print(type(len(configData.wareConfigData["wareType"])))

# for i in configData.wareConfigData["wareName"]:
#     print(i)

#         def selectYl(self,Dialog):
#         self.role.setEnabled(False)
#         self.isTeam.setEnabled(False)
if "111":
    print("False")
else:
    print("true")
# flag = False
# def fun1():
#     print("1")
#     return False
# def fun2():
#     global flag
#     flag = fun1()
#     if(not flag):
#         fun1()
#         return
#     print("2")
# fun2()
0.12 <0.5 <5
print(configData.wareConfigData["matchImg"]["status"][0])