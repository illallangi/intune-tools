from pathlib import Path

from asgiref.sync import async_to_sync

from kiota_abstractions.base_request_configuration import RequestConfiguration

from kiota_serialization_json.json_serialization_writer import JsonSerializationWriter

from msgraph_beta.generated.device_management.configuration_policies.item.assignments.assignments_request_builder import (
    AssignmentsRequestBuilder,
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


class PolicyAssignmentClient:
    @async_to_sync
    async def get_configuration_policy_assignment(
        self,
        *args,
    ):
        query_params = (
            AssignmentsRequestBuilder.AssignmentsRequestBuilderGetQueryParameters(
                select=[
                    "*",
                ],
            )
        )

        request_configuration = RequestConfiguration(
            query_parameters=query_params,
        )

        for arg in args:
            next_link = None
            if arg not in cache:
                cache[arg] = {
                    "assignments": [],
                    "assignmentCount": 0,
                    "id": arg,
                }
                while True:
                    if next_link:
                        result = (
                            await self.client.device_management.configuration_policies.by_device_management_configuration_policy_id(
                                arg,
                            )
                            .assignments.with_url(
                                next_link,
                            )
                            .get(
                                request_configuration=request_configuration,
                            )
                        )
                    else:
                        result = await self.client.device_management.configuration_policies.by_device_management_configuration_policy_id(
                            arg,
                        ).assignments.get(
                            request_configuration=request_configuration,
                        )
                    writer = JsonSerializationWriter()
                    result.serialize(writer)
                    result = orjson.loads(writer.get_serialized_content())
                    for obj in result["value"]:
                        cache[arg]["assignments"].append(obj)
                        cache[arg]["assignmentCount"] = len(cache[arg]["assignments"])

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
                    "@odata.type": "#microsoft.graph.deviceManagementConfigurationPolicyAssignment",
                },
            )
            for arg in cache
            for obj in cache[arg]["assignments"]
            if arg in args
        ]
