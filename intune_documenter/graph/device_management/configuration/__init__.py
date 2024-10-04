from .category import CategoryClient
from .policy_assignment import PolicyAssignmentClient
from .policy import PolicyClient
from .policy_setting import PolicySettingClient
from .setting import SettingClient


class ConfigurationClient(
    CategoryClient,
    PolicyAssignmentClient,
    PolicyClient,
    PolicySettingClient,
    SettingClient,
):
    def __init__(self, parent):
        self.parent = parent

    @property
    def client(self):
        return self.parent.client
