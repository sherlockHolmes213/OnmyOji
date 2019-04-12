import yuling
import configData
import time

def missionJun():
    # if(not configData.wareConfigData["isLock"]):
    #     yuling.isLock()
    if(configData.flag == 1):
        if(configData.wareType == 2):
            if(configData.wareConfigData["isParty"] and configData.wareConfigData["role"] == "captain"):
                return yuling.missionStart()
            else:
                configData.flag = 2
        else:
            return yuling.missionStart()
    elif(configData.flag == 2):
        return yuling.missionAccount()
    else:
        return yuling.missionEnd()
       

