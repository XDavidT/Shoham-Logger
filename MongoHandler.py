from EvtManagerClass import *

def db_connection():
    try:
        # TODO: fix pushing to DB
        meg.register_connection(alias='default',name ='test',host = '192.168.0.128',port = 27017)

    except:
        print("Fail to connect DB")

def db_stopConnection():
    meg.disconnect('default')