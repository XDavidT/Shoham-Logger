import grpc
from concurrent import futures
import evtmanager_pb2
import evtmanager_pb2_grpc

def startConnection():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    evtmanager_pb2_grpc.add_RouteGuideServicer_to_server()









if __name__ == '__main__':
    startConnection()