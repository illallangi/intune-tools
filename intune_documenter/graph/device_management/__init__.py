from functools import cached_property

from .configuration import ConfigurationClient


class DeviceManagementClient:
    def __init__(self, parent):
        self.parent = parent

    @property
    def client(self):
        return self.parent.client

    @cached_property
    def configuration(self):
        return ConfigurationClient(self)
