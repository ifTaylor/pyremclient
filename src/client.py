from src.remote import Remote
from config import Service

class Client:
    def __init__(
        self,
        remote: Remote
    ) -> None:
        self.remote = remote

    #remote proceedure call
    def call_greeter(self, service, **data):
        for service_obj in self.remote.services:
            if service_obj.name == service:
                # Create a copy of the service elements
                elements = service_obj.elements.copy()

                # Update the elements with the values from the data dictionary
                for name, value in data.items():
                    if name in elements:
                        elements[name] = value

                # Create a new Service object with the updated elements
                updated_service = Service(
                    name=service_obj.name,
                    stub=service_obj.stub,
                    call=service_obj.call,
                    request=service_obj.request,
                    elements=elements
                )

                # Call the remote_call function with the updated service
                response = self.remote.remote_call(updated_service)

                return response

        return None
