from EvtManagerClass import *
from datetime import datetime

def db_connection():
    try:
        meg.register_connection(alias='default',
                                name ='clientManager',
                                host = 'mongo.davidt.net',
                                port = 27018 )
        print("Mongo try to connect") # Debug only
    except:
        print("Fail to connect DB") # Debug only

def pushToMongo(evtmgr) -> bool:
    loghand = LogTemplate() # LogHandler in the Class
    loghand.logid = evtmgr.id
    loghand.client_time = datetime.fromtimestamp(evtmgr.time.seconds)  #TODO: check if the convert is right
    loghand.insert_time = datetime.now()
    loghand.type = evtmgr.type
    loghand.src = evtmgr.src
    loghand.cat = evtmgr.cat
    loghand.hostname = evtmgr.hostname
    loghand.username = evtmgr.username
    loghand.os = evtmgr.os
    loghand.ip_add = evtmgr.ip_add
    loghand.mac_add = evtmgr.mac_add
    if (evtmgr.dataList != None):
        loghand.dataList = list(evtmgr.dataList)

    try:
        loghand.save()
        return True
    except Exception as error_massage:
        print('Push_to_mongo failure:\n %s' % error_massage) # Debug only
        return False


def db_stopConnection():
    meg.disconnect('default')