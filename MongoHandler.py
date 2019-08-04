from EvtManagerClass import *

def db_connection():
    try:
        # TODO: fix pushing to DB
        meg.register_connection(alias='default',name ='test',host = '192.168.0.128',port = 27017)
        print("Mongo try to connect")

    except:
        print("Fail to connect DB")

def pushToMongo(evtmgr) -> LogTemplate:
    loghand = LogTemplate()
    loghand.id = evtmgr.id
    loghand.time = evtmgr.time
    loghand.type = evtmgr.type
    loghand.src = evtmgr.src
    loghand.hostname = evtmgr.hostname
    loghand.username = evtmgr.username
    loghand.os = evtmgr.os
    if (evtmgr.dataList != None):
        loghand.dataList = evtmgr.dataList
    try:
        loghand.save()
        print("OK")  # For debug only
        return True
    except:
        return False


def db_stopConnection():
    meg.disconnect('default')