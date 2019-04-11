import yuling
import configData
import time

def missionJun():
    if(not configData.wareConfigData["isLock"]):
            yuling.isLock()
    if(configData.flag == 1):
        if(configData.wareType == 2):
            if(configData.wareConfigData["isParty"] and configData.wareConfigData["role"] == "captain"):
                yuling.missionStart()
            else:
                configData.flag = 2
        else:
            yuling.missionStart()
    elif(configData.flag == 2):
        yuling.missionAccount()
    else:
        yuling.missionEnd()
       

