from intune_documenter.graph_object import GraphObject


class Policy(GraphObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.createdDateTime = kwargs.pop("createdDateTime")
        self.description = kwargs.pop("description")
        self.id = kwargs.pop("id")
        self.lastModifiedDateTime = kwargs.pop("lastModifiedDateTime")
        self.name = kwargs.pop("name")
        self.roleScopeTagIds = kwargs.pop("roleScopeTagIds")
        self.settingCount = kwargs.pop("settingCount")
        self.templateReference = kwargs.pop("templateReference")

        super().__init__(
            **kwargs,
        )
