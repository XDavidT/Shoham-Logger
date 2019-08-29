from concurrent import futures
import grpc, time
from ProtoBuf import evtmanager_pb2_grpc,evtmanager_pb2
from MongoHandler import *

class informationExchangeServicer(evtmanager_pb2_grpc.informationExchangeServicer):

    def __init__(self):
        pass

    def PushLog(self, request, context):
        print("Pusher has been used !") # For debug only
        if(pushToMongo(request)):
            return evtmanager_pb2.ack(isDeliver=True)  # TCP Style
        else:
            return evtmanager_pb2.ack(isDeliver=False)

    def getInfo(self, request, context):
        print("Request for Category's") # For debug only
        cat_massage = evtmanager_pb2.information()
        cat_list = cat_massage.category
        # static for now # debug only
        cat_list.append('Security')
        cat_list.append('Application')
        return cat_massage

def startConnection():  # Server to connect with client
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    evtmanager_pb2_grpc.add_informationExchangeServicer_to_server(informationExchangeServicer(), server)
    server.add_insecure_port('[::]:50051')
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