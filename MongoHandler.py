import mongoengine as meg

def db_connection():
    try:
        meg.register_connection(alias='clientManager',
                                host = 'mongodb+srv://siem:iCDoqbyTT3xh@cluster0-ecrrx.gcp.mongodb.net/clientManager?retryWrites=true&w=majority')
        meg.register_connection(alias='policyManager',
                                host='mongodb+srv://siem:iCDoqbyTT3xh@cluster0-ecrrx.gcp.mongodb.net/policyManager?retryWrites=true&w=majority')
        print("Mongo connected") # Debug only
    except Exception as e:
        print("Fail to connect DB\n"+str(e)) # Debug only

def db_stopConnection():
    meg.disconnect('clientManager')


# pip install pymongo[srv] Must use to srv