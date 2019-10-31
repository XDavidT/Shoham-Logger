import datetime
from MongoC.EvtManagerClass import LogTemplate
from MongoC.ClientReport import ClientReport as ClientR
from MongoC.CategoryClass import Category

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

def PushClientReports(ClientReport)->bool:
    clientReport = ClientR()
    clientReport.header = ClientReport.head
    clientReport.desc = ClientReport.details
    clientReport.time = datetime.now()
    try:
        clientReport.save()
        return True
    except Exception as error_massage:
        print('Push_to_mongo failure:\n %s' % error_massage)  # Debug only
        return False

def get_categories(information):
    cat_class = Category.objects.get()
    for category in cat_class.category_select:
        information.append(category)
    return information
