import mongoengine as meg
def db_connection():
    meg.register_connection(
        alias='azure',
        username='db-admin',
        password='xfeDZ{}Js4zw',
        host='52.168.9.175',
        port='27017'
    )