import mongoengine as meg

meg.connect(host='mongodb+srv://siem:iCDoqbyTT3xh@cluster0-ecrrx.gcp.mongodb.net/clientManager?retryWrites=true&w=majority',
            alias='clientManager',db='clientManager')

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
        'db_alias': 'clientManager',
        'collection': 'clientLog'
    }