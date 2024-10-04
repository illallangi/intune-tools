from abc import ABC


class GraphObject(ABC):
    def __init__(
        self,
        **kwargs,
    ):
        self.client = kwargs.pop("client")
        self.type = kwargs.pop("@odata.type")

        if kwargs:
            raise ValueError(
                f"Unknown kwargs for {self.type}: {', '.join(kwargs.keys())}"
            )

    def __str__(self):
        return str(self.type)


class GraphSettingInstanceObject(GraphObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.policyId = kwargs.pop("policyId")
        self.settingDefinitionId = kwargs.pop("settingDefinitionId")
        self.settingInstanceTemplateReference = kwargs.pop(
            "settingInstanceTemplateReference"
        )

        super().__init__(
            **kwargs,
        )
