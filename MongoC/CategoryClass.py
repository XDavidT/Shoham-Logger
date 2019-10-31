import mongoengine as meg

class Category(meg.Document):
    category_select = meg.ListField(required=True)
    meta = {
        'alias': 'policyManager',
        'collection': 'category'
    }