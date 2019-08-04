import mongoengine as meg

class LogTemplate(meg.Document):
    id = meg.IntField(required=True)
    time = meg.DateTimeField(required=True)
    type = meg.IntField(required=True)
    src = meg.StringField(required=True)
    cat = meg.IntField(required=True)
    dataList = meg.ListField()
    hostname = meg.StringField(required=True)
    username = meg.StringField()
    os = meg.StringField()

    meta = {
        'alias': 'default',
        'collection': 'clientLog'
    }