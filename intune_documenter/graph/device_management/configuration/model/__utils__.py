from .category import Category
from .choice_setting import ChoiceSettingCollectionDefinition
from .choice_setting import ChoiceSettingCollectionInstance
from .choice_setting import ChoiceSettingDefinition
from .choice_setting import ChoiceSettingInstance
from .choice_setting import ChoiceSettingValue
from .group_setting import GroupSettingCollectionDefinition
from .group_setting import GroupSettingCollectionInstance
from .group_setting import GroupSettingDefinition
from .group_setting import GroupSettingInstance
from .group_setting import GroupSettingValue
from .policy import Policy
from .policy_assignment import PolicyAssignment
from .policy_setting import PolicySetting
from .redirect_setting import RedirectSettingCollectionDefinition
from .redirect_setting import RedirectSettingCollectionInstance
from .redirect_setting import RedirectSettingDefinition
from .redirect_setting import RedirectSettingInstance
from .redirect_setting import RedirectSettingValue
from .simple_setting import SimpleSettingCollectionDefinition
from .simple_setting import SimpleSettingCollectionInstance
from .simple_setting import SimpleSettingDefinition
from .simple_setting import SimpleSettingInstance
from .simple_setting import SimpleSettingValue


def from_dict(
    client,
    **kwargs,
):
    if "@odata.type" not in kwargs:
        raise ValueError("Object does not have @odata.type.")

    type_map = {
        "#microsoft.graph.deviceManagementConfigurationCategory": Category,
        "#microsoft.graph.deviceManagementConfigurationChoiceSettingCollectionDefinition": ChoiceSettingCollectionDefinition,
        "#microsoft.graph.deviceManagementConfigurationChoiceSettingCollectionInstance": ChoiceSettingCollectionInstance,
        "#microsoft.graph.deviceManagementConfigurationChoiceSettingDefinition": ChoiceSettingDefinition,
        "#microsoft.graph.deviceManagementConfigurationChoiceSettingInstance": ChoiceSettingInstance,
        "#microsoft.graph.deviceManagementConfigurationChoiceSettingValue": ChoiceSettingValue,
        "#microsoft.graph.deviceManagementConfigurationGroupSettingCollectionInstance": GroupSettingCollectionInstance,
        "#microsoft.graph.deviceManagementConfigurationGroupSettingDefinition": GroupSettingDefinition,
        "#microsoft.graph.deviceManagementConfigurationGroupSettingInstance": GroupSettingInstance,
        "#microsoft.graph.deviceManagementConfigurationGroupSettingValue": GroupSettingValue,
        "#microsoft.graph.deviceManagementConfigurationPolicy": Policy,
        "#microsoft.graph.deviceManagementConfigurationPolicyAssignment": PolicyAssignment,
        "#microsoft.graph.deviceManagementConfigurationPolicySetting": PolicySetting,
        "#microsoft.graph.deviceManagementConfigurationRedirectSettingCollectionDefinition": RedirectSettingCollectionDefinition,
        "#microsoft.graph.deviceManagementConfigurationRedirectSettingCollectionInstance": RedirectSettingCollectionInstance,
        "#microsoft.graph.deviceManagementConfigurationRedirectSettingDefinition": RedirectSettingDefinition,
        "#microsoft.graph.deviceManagementConfigurationRedirectSettingInstance": RedirectSettingInstance,
        "#microsoft.graph.deviceManagementConfigurationRedirectSettingValue": RedirectSettingValue,
        "#microsoft.graph.deviceManagementConfigurationSettingGroupCollectionDefinition": GroupSettingCollectionDefinition,
        "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionDefinition": SimpleSettingCollectionDefinition,
        "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionInstance": SimpleSettingCollectionInstance,
        "#microsoft.graph.deviceManagementConfigurationSimpleSettingDefinition": SimpleSettingDefinition,
        "#microsoft.graph.deviceManagementConfigurationSimpleSettingInstance": SimpleSettingInstance,
        "#microsoft.graph.deviceManagementConfigurationSimpleSettingValue": SimpleSettingValue,
    }

    if kwargs["@odata.type"] in type_map:
        return type_map[kwargs["@odata.type"]](
            client=client,
            **kwargs,
        )

    raise NotImplementedError(kwargs["@odata.type"])
