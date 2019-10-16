import mongoengine as meg
from datetime import datetime

class LogTemplate(meg.Document):
    logid = meg.StringField(required=True)
    client_time = meg.DateTimeField(required=True)
    insert_time = meg.DateTimeField(requierd=True)
    type = meg.StringField(required=True)
    src = meg.StringField(required=True)
    cat = meg.StringField(required=True)
    dataList = meg.ListField()
    hostname = meg.StringField(required=True)
    username = meg.StringField()
    os = meg.StringField(required=True)
    ip_add = meg.StringField(required=True)
    mac_add = meg.StringField(required=True)

    meta = {
        'alias': 'default',
        'collection': 'clientLog'
    }