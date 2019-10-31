import mongoengine as meg

class ClientReport(meg.Document):
    header = meg.StringField(required=True)
    desc = meg.StringField(required=True)
    time = meg.DateTimeField(required=True)
    meta = {
        'alias': 'clientManager',
        'collection': 'ClientReports'
    }