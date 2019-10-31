from concurrent import futures
import grpc, time
from ProtoBuf import evtmanager_pb2_grpc,evtmanager_pb2
from MongoHandler import db_connection, db_stopConnection
from ServerActions import *

class informationExchangeServicer(evtmanager_pb2_grpc.informationExchangeServicer):

    def __init__(self):
        pass

    def PushLog(self, request, context):
        if(pushToMongo(request)):
            return evtmanager_pb2.ack(isDeliver=True)  # TCP Style
        else:
            return evtmanager_pb2.ack(isDeliver=False)

    def getInfo(self, request, context):
        print("Request for Category's") # For debug only
        cat_massage = evtmanager_pb2.information()
        cat_list = cat_massage.category
        return get_categories(cat_list)

    def PushClientReports(self,request,context):
        if(PushClientReports(request)):
            return evtmanager_pb2.ack(isDeliver=True)  # TCP Style
        else:
            return evtmanager_pb2.ack(isDeliver=False)

def startConnection():  # Server to connect with client
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    with open("Keys\server.key",'rb') as f:
        private_key = f.read()
    with open("Keys\server.crt",'rb') as f:
        public_key = f.read()
    evtmanager_pb2_grpc.add_informationExchangeServicer_to_server(informationExchangeServicer(), server)
    server_credentials = grpc.ssl_server_credentials(((private_key,public_key),))
    server.add_secure_port('[::]:50051',server_credentials)
    # server.add_insecure_port('[::]:50051')
    server.start()
    db_connection()
    try:
        while True:
            # TODO: set normal timer
            print('Server is UP !')
            time.sleep(3600)
    except KeyboardInterrupt:
        db_stopConnection()
        server.stop(0)


if __name__ == '__main__':
    startConnection()