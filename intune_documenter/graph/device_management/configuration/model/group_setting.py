from intune_documenter.graph_object import GraphObject, GraphSettingInstanceObject


class GroupSettingCollectionDefinition(GraphObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.applicability = kwargs.pop("applicability")
        self.baseUri = kwargs.pop("baseUri")
        self.categoryId = kwargs.pop("categoryId")
        self.childIds = kwargs.pop("childIds")
        self.dependedOnBy = kwargs.pop("dependedOnBy")
        self.dependentOn = kwargs.pop("dependentOn")
        self.description = kwargs.pop("description", None)
        self.displayName = kwargs.pop("displayName")
        self.id = kwargs.pop("id")
        self.infoUrls = kwargs.pop("infoUrls")
        self.keywords = kwargs.pop("keywords")
        self.maximumCount = kwargs.pop("maximumCount")
        self.minimumCount = kwargs.pop("minimumCount")
        self.name = kwargs.pop("name")
        self.offsetUri = kwargs.pop("offsetUri")
        self.referredSettingInformationList = kwargs.pop(
            "referredSettingInformationList"
        )
        self.rootDefinitionId = kwargs.pop("rootDefinitionId")
        self.uxBehavior = kwargs.pop("uxBehavior")
        self.version = kwargs.pop("version")
        self.occurance = (
            kwargs.pop("occurence")
            if "occurence" in kwargs
            else kwargs.pop("occurrence", None)
        )
        self.helpText = kwargs.pop("helpText", None)

        super().__init__(
            **kwargs,
        )


class GroupSettingCollectionInstance(GraphSettingInstanceObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.groupSettingCollectionValue = kwargs.pop("groupSettingCollectionValue")
        super().__init__(
            **kwargs,
        )


class GroupSettingDefinition(GraphObject):
    def __init__(
        self,
        **kwargs,
    ):
        super().__init__(
            **kwargs,
        )


class GroupSettingInstance(GraphSettingInstanceObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.groupSettingValue = kwargs.pop("groupSettingValue")
        super().__init__(
            **kwargs,
        )


class GroupSettingValue(GraphObject):
    def __init__(
        self,
        **kwargs,
    ):
        super().__init__(
            **kwargs,
        )
