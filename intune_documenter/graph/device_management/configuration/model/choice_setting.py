from intune_documenter.graph_object import GraphObject, GraphSettingInstanceObject

from more_itertools import one


class ChoiceSettingCollectionDefinition(GraphObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.applicability = kwargs.pop("applicability")
        self.baseUri = kwargs.pop("baseUri")
        self.categoryId = kwargs.pop("categoryId")
        self.defaultOptionId = kwargs.pop("defaultOptionId", None)
        self.description = kwargs.pop("description", None)
        self.displayName = kwargs.pop("displayName")
        self.id = kwargs.pop("id")
        self.infoUrls = kwargs.pop("infoUrls")
        self.keywords = kwargs.pop("keywords")
        self.maximumCount = kwargs.pop("maximumCount")
        self.minimumCount = kwargs.pop("minimumCount")
        self.name = kwargs.pop("name")
        self.offsetUri = kwargs.pop("offsetUri")
        self.options = kwargs.pop("options")
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


class ChoiceSettingCollectionInstance(GraphSettingInstanceObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.choiceSettingCollectionValue = kwargs.pop("choiceSettingCollectionValue")
        super().__init__(
            **kwargs,
        )


class ChoiceSettingDefinition(GraphObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.id = kwargs.pop("id")
        self.applicability = kwargs.pop("applicability")
        self.baseUri = kwargs.pop("baseUri")
        self.categoryId = kwargs.pop("categoryId")
        self.displayName = kwargs.pop("displayName")
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
        self.defaultOptionId = kwargs.pop("defaultOptionId", None)
        self.options = kwargs.pop("options")
        self.helpText = kwargs.pop("helpText", None)
        self.occurrence = (
            kwargs.pop("occurence")
            if "occurence" in kwargs
            else kwargs.pop("occurrence", None)
        )
        self.description = kwargs.pop("description", None)

        super().__init__(
            **kwargs,
        )


class ChoiceSettingInstance(GraphSettingInstanceObject):
    def __init__(
        self,
        client,
        **kwargs,
    ):
        from .__utils__ import from_dict

        self.choiceSettingValue = from_dict(
            client,
            **kwargs.pop("choiceSettingValue"),
        )

        super().__init__(
            client=client,
            **kwargs,
        )

    def __str__(self):
        return one(
            [
                option
                for option in one(
                    self.client.get_configuration_setting(self.settingDefinitionId)
                ).options
                if option["itemId"] == self.choiceSettingValue.value
            ]
        ).get("displayName")


class ChoiceSettingValue(GraphObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.children = kwargs.pop("children")
        self.settingValueTemplateReference = kwargs.pop("settingValueTemplateReference")
        self.value = kwargs.pop("value")

        super().__init__(
            **kwargs,
        )
