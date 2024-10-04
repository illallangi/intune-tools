from functools import cached_property

from azure.identity.aio import EnvironmentCredential

from dotenv import load_dotenv

from msgraph_beta import GraphServiceClient

from .device_management import DeviceManagementClient

load_dotenv()


class GraphClient:
    @property
    def scopes(self):
        return [
            "https://graph.microsoft.com/.default",
        ]

    @cached_property
    def credential(self):
        return EnvironmentCredential()

    @cached_property
    def client(self):
        return GraphServiceClient(
            self.credential,
            self.scopes,
        )

    @cached_property
    def device_management(self):
        return DeviceManagementClient(self)
