import mongoengine as meg
from datetime import datetime

class LogTemplate(meg.Document):
    id = meg.SequenceField(primary_key=True)
    logid = meg.IntField(required=True)
    client_time = meg.DateTimeField(required=True)
    insert_time = meg.DateTimeField(requierd=True)
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