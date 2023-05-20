from grpc_tools import protoc
protoc.main([
    'grpc_tools.protoc',
    '-I{}'.format('./src/proto'),
    '--python_out={}'.format('./src/proto/'),
    '--grpc_python_out={}'.format('./src/proto'),
    './src/proto/pyremclient_proto.proto'
])

from config import (
    ClientSettings,
    Service
)

from src import Client
from src.remote import Remote

if __name__ == "__main__":
    remote = Remote(
        server_ip=ClientSettings.ip,
        server_port=ClientSettings.port,
        services=Service.services()
    )

    client = Client(
        remote=remote
    )

    data = {
        "name": "GeneralKenobi",
    }

    response = client.call_greeter(service="service1", **data)
    print(response)
