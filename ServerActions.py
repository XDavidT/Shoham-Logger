import datetime,pytz
from MongoC.EvtManagerClass import LogTemplate
from MongoC.ClientReport import ClientReport as ClientR
from MongoC.CategoryClass import Category

timezone = pytz.timezone('Asia/Tel_Aviv')
def pushToMongo(evtmgr) -> bool:
    loghand = LogTemplate() # LogHandler in the Class
    loghand.logid = evtmgr.id
    loghand.client_time = datetime.datetime.fromtimestamp(evtmgr.time.seconds, timezone)  #TODO: check if the convert is right
    loghand.insert_time = datetime.datetime.now()
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
    clientReport.time = datetime.datetime.now()
    try:
        clientReport.save()
        return True
    except Exception as error_massage:
        print('Push_to_mongo failure:\n %s' % error_massage)  # Debug only
        return False

def get_categories():
    cat_class = Category.objects.first()
    cat_list = []
    for category in cat_class.category_select:
        cat_list.append(category)
    return cat_list
