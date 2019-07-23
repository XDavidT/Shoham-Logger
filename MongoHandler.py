import mongoengine

def connection():
    mongoengine.register_connection(alias='core')
    # TODO: Complete connection