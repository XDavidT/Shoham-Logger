from EvtManagerClass import *
from datetime import datetime

def db_connection():
    try:
        # TODO: fix pushing to DB
        meg.register_connection(alias='default',name ='test',host = '192.168.0.128',port = 27017)
        print("Mongo try to connect")# Debug only

    except:
        print("Fail to connect DB") # Debug only

def pushToMongo(evtmgr) -> LogTemplate:
    loghand = LogTemplate() # LogHandler in the Class
    loghand.logid = evtmgr.id
    loghand.time = datetime.fromtimestamp(evtmgr.time.seconds)
    loghand.type = evtmgr.type
    loghand.src = evtmgr.src
    loghand.cat = evtmgr.cat
    loghand.hostname = evtmgr.hostname
    loghand.username = evtmgr.username
    loghand.os = evtmgr.os


    try:
        if (evtmgr.dataList != None):
            loghand.dataList = list(evtmgr.dataList)
        loghand.save()
        return True
    except Exception as error_massage:
        print('Push_to_mongo failure:\n %s' % error_massage) # Debug only
        return False


def db_stopConnection():
    meg.disconnect('default')