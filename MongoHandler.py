from EvtManagerClass import *
from datetime import datetime

def db_connection():
    try:
        meg.register_connection(alias='default',
                                host = 'mongodb+srv://siem:iCDoqbyTT3xh@cluster0-ecrrx.gcp.mongodb.net/clientManager?retryWrites=true&w=majority')
        print("Mongo connected") # Debug only
    except Exception as e:
        print("Fail to connect DB\n"+e) # Debug only

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


# pip install pymongo[srv] Must use to srv