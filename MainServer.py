from concurrent import futures
import grpc
from ProtoBuf import evtmanager_pb2_grpc,evtmanager_pb2
from EvtManagerClass import LogTemplate, db_connection


class PusherServicer(evtmanager_pb2_grpc.PusherServicer):

    def __init__(self):
        db_connection()

    def PushLog(self, request, context):
        try:
            log = LogTemplate()
            log.id = request.id
            log.time = request.time
            log.type = request.type
            log.src = request.src
            log.hostname = request.hostname
            log.username = request.username
            log.os = request.os
            if (request.dataList != None):
                log.dataList = request.dataList
            log.save()
            return evtmanager_pb2.ack(isDeliver=True)   # TCP Style
        except:
            return evtmanager_pb2.ack(isDeliver = False)  # TCP Style

def startConnection():  # Server to connect with client
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    evtmanager_pb2_grpc.add_PusherServicer_to_server(PusherServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

if __name__ == '__main__':
    startConnection()