import mongoengine as meg

meg.connect(host='mongodb://siem.davidt.net:27018',
            alias='policyManager',db='policyManager')
class Category(meg.Document):
    category_select = meg.ListField(required=True)
    meta = {
        'db_alias': 'policyManager',
        'collection': 'category'
    }