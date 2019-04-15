import match
import configData
import mouseEvent
import time
import pyautogui
import random



def missionStart():
    configData.returnFlag = match.template_image("a.png","images/" + configData.wareConfigData["matchImg"]["status"][0][configData.wareType]+".png")
    if(configData.returnFlag):
        missionIng()
    else:
        return
def missionAccount():
    configData.returnFlag = match.template_image("a.png","images/"+ configData.wareConfigData["matchImg"]["status"][1] + ".png")
    if(configData.returnFlag):
        missionIng()
    else:
        return
def missionEnd():
    configData.returnFlag = match.template_image("a.png","images/"+ configData.wareConfigData["matchImg"]["status"][2] + ".png")
    if(configData.returnFlag):
        missionIng()
    else:
        return

def missionInvite():
    print("自动邀请")
    configData.wareConfigData["isAutoInvite"] = match.template_image("a.png","images/"+ configData.wareConfigData["matchImg"]["autoInvite"] + ".png")
    mouseEvent.mouseMove(configData.tl,configData.tw,configData.th,0)
    pyautogui.click(duration=0.25)
    time.sleep(2)
    inviteSuree()
def missionInviteAccept():
    print("接受邀请")
    configData.wareConfigData["isAtoAcceptInvite"] = match.template_image("a.png","images/"+ configData.wareConfigData["matchImg"]["autoAcceptInvite"] + ".png")
    if(configData.returnFlag):
        mouseEvent.mouseMove(configData.tl,configData.tw,configData.th,0)
        pyautogui.click(duration=0.25)
    else:
        return
    # time.sleep(2)
def inviteSuree():
    print("确认邀请")
    match.template_image("a.png","images/"+ configData.wareConfigData["matchImg"]["sure"] + ".png")
    mouseEvent.mouseMove(configData.tl,configData.tw,configData.th,0)
    pyautogui.click(duration=0.25)
    time.sleep(2)
def isLock():
    configData.wareConfigData["isLock"] = match.template_image("a.png","images/"+ configData.wareConfigData["matchImg"]["lock"] + ".png")
    if(configData.wareConfigData["isLock"]):
        lockAction()
    configData.wareConfigData["isLock"] = True
    
def missionIng():
    import init
    # if(not configData.returnFlag):
    #     init.window_capture("a.png",False)
    #     configData.returnFlag = match.template_image("a.png","")
    #     return
    if(configData.flag == 1):
        print("战斗开始")
        mouseEvent.mouseMove(configData.tl,configData.tw,configData.th,0)
        mouseEvent.mouseClick()
        configData.flag = 2
        time.sleep(configData.wareConfigData["sleepTime"][configData.wareType])
        # return init.window_capture("a.png")
    elif(configData.flag == 2):
        print("战斗结算")
        mouseEvent.mouseMove(configData.tl,configData.tw,configData.th,0)
        mouseEvent.mouseClick()
        pyautogui.click(duration=0.25)
        time.sleep(0.5)
        configData.flag = 3
        # return init.window_capture("a.png")
    else:
        print("战斗结束")
        mouseEvent.mouseMove(configData.tl,configData.tw,configData.th,1)
        mouseEvent.mouseClick()
        pyautogui.click(duration=0.25)
        time.sleep(0.5)
        pyautogui.click(duration=0.25)
        # init.window_capture("a.png",False)
        # if(configData.wareConfigData["role"] == "captain" and not configData.wareConfigData["isAutoInvite"] and configData.wareType==2):
        #     time.sleep(2)
        #     missionInvite()
        # elif(configData.wareConfigData["role"] == "member" and not configData.wareConfigData["isAtoAcceptInvite"] and configData.wareType==2):
        #     time.sleep(2)
        #     missionInviteAccept()
        configData.flag = 1
        configData.count = configData.count + 1
        print("正在刷 %s ,已经进行 %d 次"%(configData.wareConfigData["wareName"][configData.wareType],configData.count))
        # init.window_capture("a.png")
def lockAction():
    print("锁定阵容")
    mouseEvent.mouseMove(configData.tl,configData.tw,configData.th,0)
    pyautogui.click(duration=0.25)