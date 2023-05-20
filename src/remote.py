import grpc

class Remote:
    def __init__(
        self,
        server_ip: str,
        server_port: int,
        services: dict,
    ) -> None:
        self.server_ip = server_ip
        self.server_port = server_port
        self.services = services
    
    def remote_call(self, service_data):
        channel = grpc.insecure_channel(f'{self.server_ip}:{self.server_port}')
        stub = service_data.stub(channel)
        request = service_data.request()

        for element_key, value in service_data.elements.items():
            setattr(request, element_key, value.strip())

        response = getattr(stub, service_data.call)(request)

        return response



