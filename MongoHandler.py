import mongoengine as meg
def db_connection():
    try:
        # TODO: fix pushing to DB
        meg.register_connection(
            alias='default',
            username='db-admin',
            password='xfeDZ{}Js4zw',
            host='40.114.121.17/test',
            port='27017',
            db='test'
        )
        print("DB connection success")
    except:
        print("Fail to connect DB")