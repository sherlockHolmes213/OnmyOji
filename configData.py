flag = 1
# 战斗状态 1：战斗开始 2：战斗结算 3：战斗结
wareType = 2
# 战斗类型 0：御灵 1：业原火 2御魂
sleepTime = 30
# 战斗时间和战斗类型相对应1：御灵 2：业原火 3：御魂
# "role":"captain"队长 "member"队员
wareConfigData = {
    "flag":[1,2.3],
    "wareType":[1,2.3],
    "wareName":["御灵","业原火","御魂"],
    "sleepTime":[30,60,30],
    "autoInvite":True,
    "acceptInvite":True,
    "isParty":True,
    "role":"member",
    "isLock":False,
    "isAtoAcceptInvite":False,
    "isAutoInvite":False,
    "matchImg":{
        "status":[["yl","yl","yh"],"account","end"],
        "lock":"unlock",
        "autoInvite":"autoInvite",
        "autoAcceptInvite":"inviteAcceptLock",
        "sure":"sure"
    }
}
tl = []
th = ""
tw = ""
count = 0
matchResult = False
tplImgTemp = ""
returnFlag = False
prtscFlag = True