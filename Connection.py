from concurrent import futures
import grpc
import evtmanager_pb2
import evtmanager_pb2_grpc


class RouteGuideServicer(evtmanager_pb2_grpc.RouteGuideServicer):

    def __init__(self):
        # TODO: Add connection to DB
        pass









def startConnection():  # Server to connect with client
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    evtmanager_pb2_grpc.add_RouteGuideServicer_to_server(RouteGuideServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

if __name__ == '__main__':
    startConnection()