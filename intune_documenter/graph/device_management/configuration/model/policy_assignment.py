from intune_documenter.graph_object import GraphObject


class PolicyAssignment(GraphObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.id = kwargs.pop("id")
        self.source = kwargs.pop("source")
        self.sourceId = kwargs.pop("sourceId")
        self.target = kwargs.pop("target")
        self.policyId = kwargs.pop("policyId")

        super().__init__(
            **kwargs,
        )
