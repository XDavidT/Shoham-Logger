import mongoengine as meg

meg.connect(host='mongodb://siem.davidt.net:27018',
            alias='clientManager',db='clientManager')

class ClientReport(meg.Document):
    header = meg.StringField(required=True)
    desc = meg.StringField(required=True)
    time = meg.DateTimeField(required=True)
    hostname = meg.StringField(required=True)
    meta = {
        'db_alias': 'clientManager',
        'collection': 'ClientReports'
    }