from pathlib import Path

from asgiref.sync import async_to_sync

from kiota_abstractions.base_request_configuration import RequestConfiguration

from kiota_serialization_json.json_serialization_writer import JsonSerializationWriter

from msgraph_beta.generated.device_management.configuration_settings.configuration_settings_request_builder import (
    ConfigurationSettingsRequestBuilder,
)

import orjson

from .model import from_dict


cache_path = Path.cwd().joinpath(
    f"{__name__.split('.')[-1]}.json",
)
cached_all = False
cache = {}
if cache_path.exists():
    with cache_path.open("rb") as file:
        cache = orjson.loads(file.read())
        cached_all = cache["all"]
        cache = cache["objects"]


def save_cache():
    with cache_path.open("wb") as file:
        file.write(
            orjson.dumps(
                {
                    "all": cached_all,
                    "count": len(cache),
                    "objects": cache,
                },
                option=orjson.OPT_INDENT_2 | orjson.OPT_SORT_KEYS,
            ),
        )


class SettingClient:
    @async_to_sync
    async def get_configuration_setting(
        self,
        *args,
    ):
        global cached_all

        query_params = ConfigurationSettingsRequestBuilder.ConfigurationSettingsRequestBuilderGetQueryParameters(
            select=[
                "*",
            ],
        )

        request_configuration = RequestConfiguration(
            query_parameters=query_params,
        )

        for arg in args or ([] if cached_all else [None]):
            next_link = None
            if not args:
                cached_all = True
            if arg not in cache:
                while True:
                    if next_link:
                        result = await self.client.device_management.configuration_settings.with_url(
                            next_link,
                        ).get(
                            request_configuration=request_configuration,
                        )
                    elif arg:
                        result = await self.client.device_management.configuration_settings.by_device_management_configuration_setting_definition_id(
                            arg,
                        ).get(
                            request_configuration=request_configuration,
                        )
                    else:
                        result = await self.client.device_management.configuration_settings.get(
                            request_configuration=request_configuration,
                        )
                    writer = JsonSerializationWriter()
                    result.serialize(writer)
                    result = orjson.loads(writer.get_serialized_content())
                    for obj in result["value"] if not arg else [result]:
                        cache[obj["id"]] = obj

                    if "@odata.nextLink" in result:
                        next_link = result["@odata.nextLink"]
                    else:
                        break

                save_cache()

        return [
            from_dict(
                self,
                **{
                    **cache[arg],
                },
            )
            for arg in cache
            if arg in args or not args
        ]
