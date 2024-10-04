from pathlib import Path

from asgiref.sync import async_to_sync

from kiota_abstractions.base_request_configuration import RequestConfiguration

from kiota_serialization_json.json_serialization_writer import JsonSerializationWriter

from msgraph_beta.generated.device_management.configuration_policies.item.settings.settings_request_builder import (
    SettingsRequestBuilder,
)

import orjson

from .model import from_dict


cache_path = Path.cwd().joinpath(
    f"{__name__.split('.')[-1]}.json",
)
cache = {}
if cache_path.exists():
    with cache_path.open("rb") as file:
        cache = orjson.loads(file.read())
        cache = cache["objects"]


def save_cache():
    with cache_path.open("wb") as file:
        file.write(
            orjson.dumps(
                {
                    "count": len(cache),
                    "objects": cache,
                },
                option=orjson.OPT_INDENT_2 | orjson.OPT_SORT_KEYS,
            ),
        )


class PolicySettingClient:
    @async_to_sync
    async def get_policy_setting(
        self,
        *args,
    ):
        query_params = SettingsRequestBuilder.SettingsRequestBuilderGetQueryParameters(
            select=[
                "*",
            ],
        )

        request_configuration = RequestConfiguration(
            query_parameters=query_params,
        )

        for arg in args:
            next_link = None
            if arg not in cache:
                cache[arg] = {
                    "id": arg,
                    "settingCount": 0,
                    "settings": [],
                }
                while True:
                    if next_link:
                        result = (
                            await self.client.device_management.configuration_policies.by_device_management_configuration_policy_id(
                                arg,
                            )
                            .settings.with_url(
                                next_link,
                            )
                            .get(
                                request_configuration=request_configuration,
                            )
                        )
                    else:
                        result = await self.client.device_management.configuration_policies.by_device_management_configuration_policy_id(
                            arg,
                        ).settings.get(
                            request_configuration=request_configuration,
                        )
                    writer = JsonSerializationWriter()
                    result.serialize(writer)
                    result = orjson.loads(writer.get_serialized_content())
                    for obj in result["value"]:
                        cache[arg]["settings"].append(obj)
                        cache[arg]["settingCount"] = len(cache[arg]["settings"])

                    if "@odata.nextLink" in result:
                        next_link = result["@odata.nextLink"]
                    else:
                        break

                save_cache()

        return [
            from_dict(
                self,
                **{
                    **obj,
                    "policyId": arg,
                    "@odata.type": "#microsoft.graph.deviceManagementConfigurationPolicySetting",
                },
            )
            for arg in cache
            for obj in cache[arg]["settings"]
            if arg in args
        ]
