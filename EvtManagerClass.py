import mongoengine as meg
from datetime import datetime

class LogTemplate(meg.Document):
    logid = meg.IntField(required=True)
    time = meg.DateTimeField(required=True)
    type = meg.IntField(required=True)
    src = meg.StringField(required=True)
    cat = meg.IntField(required=True)
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