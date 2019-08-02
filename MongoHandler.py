import mongoengine as meg
def db_connection():
    meg.register_connection(
        alias='default',
        username='db-admin',
        password='xfeDZ{}Js4zw',
        host='40.71.181.61',
        port='27017'
    )