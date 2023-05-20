import sys
sys.path.insert(1,'./src/proto')
import pyremclient_proto_pb2
import pyremclient_proto_pb2_grpc

class ClientSettings:
    name = 'Python Client'
    ip = '127.0.0.1'
    port = '5000'

class Service:
    def __init__(self, name, stub, call, request, elements):
        self.name = name
        self.stub = stub
        self.call = call
        self.request = request
        self.elements = elements

    def services():
        return [
            Service(
                name="service1",
                stub=pyremclient_proto_pb2_grpc.GreeterStub,
                call="SayHello",
                request=pyremclient_proto_pb2.HelloRequest,
                elements={
                    "name": "\nGeneralKenobi"
                }
            ),
            Service(
                name="service2",
                stub="PLCStub",
                call="AddDevice",
                request="AddDeviceRequest",
                elements={
                    "ip": "5.5.5.5",
                    "nickname": "nickname test"
                })]