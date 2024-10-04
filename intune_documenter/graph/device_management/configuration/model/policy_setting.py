from intune_documenter.graph_object import GraphObject


class PolicySetting(GraphObject):
    def __init__(
        self,
        client,
        **kwargs,
    ):
        from .__utils__ import from_dict

        self.id = kwargs.pop("id")
        self.policyId = kwargs.pop("policyId")
        self.settingInstance = from_dict(
            client,
            policyId=self.policyId,
            **kwargs.pop("settingInstance"),
        )

        super().__init__(
            client=client,
            **kwargs,
        )
