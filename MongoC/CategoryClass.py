import mongoengine as meg

meg.connect(host='mongodb+srv://siem:iCDoqbyTT3xh@cluster0-ecrrx.gcp.mongodb.net/policyManager?retryWrites=true&w=majority',
            alias='policyManager',db='policyManager')
class Category(meg.Document):
    category_select = meg.ListField(required=True)
    meta = {
        'db_alias': 'policyManager',
        'collection': 'category'
    }