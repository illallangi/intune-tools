from intune_documenter.graph_object import GraphObject, GraphSettingInstanceObject


class SimpleSettingCollectionDefinition(GraphObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.applicability = kwargs.pop("applicability")
        self.baseUri = kwargs.pop("baseUri")
        self.categoryId = kwargs.pop("categoryId")
        self.defaultValue = kwargs.pop("defaultValue", None)
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
        self.valueDefinition = kwargs.pop("valueDefinition")
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


class SimpleSettingCollectionInstance(GraphSettingInstanceObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.simpleSettingCollectionValue = kwargs.pop("simpleSettingCollectionValue")
        super().__init__(
            **kwargs,
        )


class SimpleSettingDefinition(GraphObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.id = kwargs.pop("id")
        self.applicability = kwargs.pop("applicability")
        self.baseUri = kwargs.pop("baseUri")
        self.categoryId = kwargs.pop("categoryId")
        self.description = kwargs.pop("description", None)
        self.displayName = kwargs.pop("displayName", None)
        self.infoUrls = kwargs.pop("infoUrls")
        self.keywords = kwargs.pop("keywords")
        self.name = kwargs.pop("name")
        self.offsetUri = kwargs.pop("offsetUri")
        self.referredSettingInformationList = kwargs.pop(
            "referredSettingInformationList"
        )
        self.rootDefinitionId = kwargs.pop("rootDefinitionId")
        self.uxBehavior = kwargs.pop("uxBehavior")
        self.version = kwargs.pop("version")
        self.defaultValue = kwargs.pop("defaultValue", None)
        self.dependedOnBy = kwargs.pop("dependedOnBy")
        self.dependentOn = kwargs.pop("dependentOn")
        self.valueDefinition = kwargs.pop("valueDefinition")
        self.helpText = kwargs.pop("helpText", None)
        self.occurrence = (
            kwargs.pop("occurence")
            if "occurence" in kwargs
            else kwargs.pop("occurrence", None)
        )
        self.defaultValue = kwargs.pop("defaultValue", None)

        super().__init__(
            **kwargs,
        )


class SimpleSettingInstance(GraphSettingInstanceObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.simpleSettingValue = kwargs.pop("simpleSettingValue")
        super().__init__(
            **kwargs,
        )


class SimpleSettingValue(GraphObject):
    def __init__(
        self,
        **kwargs,
    ):
        super().__init__(
            **kwargs,
        )
