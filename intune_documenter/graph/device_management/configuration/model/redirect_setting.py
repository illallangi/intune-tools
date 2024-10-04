from intune_documenter.graph_object import GraphObject, GraphSettingInstanceObject


class RedirectSettingCollectionDefinition(GraphObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.applicability = kwargs.pop("applicability")
        self.baseUri = kwargs.pop("baseUri")
        self.categoryId = kwargs.pop("categoryId")
        self.defaultValue = kwargs.pop("defaultValue")
        self.dependedOnBy = kwargs.pop("dependedOnBy")
        self.dependentOn = kwargs.pop("dependentOn")
        self.description = kwargs.pop("description")
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
        self.valueDefinition = kwargs.pop("valueDefinition")
        self.version = kwargs.pop("version")

        super().__init__(
            **kwargs,
        )


class RedirectSettingCollectionInstance(GraphSettingInstanceObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.redirectSettingCollectionValue = kwargs.pop(
            "redirectSettingCollectionValue"
        )
        super().__init__(
            **kwargs,
        )


class RedirectSettingDefinition(GraphObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.applicability = kwargs.pop("applicability")
        self.baseUri = kwargs.pop("baseUri")
        self.categoryId = kwargs.pop("categoryId")
        self.deepLink = kwargs.pop("deepLink")
        self.description = kwargs.pop("description", None)
        self.displayName = kwargs.pop("displayName")
        self.helpText = kwargs.pop("helpText")
        self.id = kwargs.pop("id")
        self.infoUrls = kwargs.pop("infoUrls")
        self.keywords = kwargs.pop("keywords")
        self.name = kwargs.pop("name")
        self.occurrence = kwargs.pop("occurrence")
        self.offsetUri = kwargs.pop("offsetUri")
        self.redirectMessage = kwargs.pop("redirectMessage")
        self.redirectReason = kwargs.pop("redirectReason")
        self.referredSettingInformationList = kwargs.pop(
            "referredSettingInformationList"
        )
        self.rootDefinitionId = kwargs.pop("rootDefinitionId")
        self.uxBehavior = kwargs.pop("uxBehavior")
        self.version = kwargs.pop("version")

        super().__init__(
            **kwargs,
        )


class RedirectSettingInstance(GraphSettingInstanceObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.redirectSettingValue = kwargs.pop("redirectSettingValue")
        super().__init__(
            **kwargs,
        )


class RedirectSettingValue(GraphObject):
    def __init__(
        self,
        **kwargs,
    ):
        super().__init__(
            **kwargs,
        )
