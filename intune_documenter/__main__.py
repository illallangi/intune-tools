import click

from more_itertools import one, only

import orjson

from tabulate import tabulate

import xlsxwriter

from .graph import GraphClient

json_flag = click.option(
    "--json",
    is_flag=True,
    help="Output as JSON",
)

ids_argument = click.argument(
    "ids",
    type=str,
    required=False,
    nargs=-1,
)


@click.group()
def main():
    pass


@main.command()
@json_flag
@ids_argument
def category(
    json,
    ids,
):
    graph = GraphClient()
    objs = graph.device_management.configuration.get_configuration_category(*ids)

    if json:
        print(
            orjson.dumps(
                [obj for obj in objs],
                option=orjson.OPT_INDENT_2,
            ).decode("utf-8"),
        )
        return

    print(
        tabulate(
            [
                {
                    "id": obj.id,
                    "path": obj.path,
                }
                for obj in sorted(
                    objs,
                    key=lambda obj: obj.path.lower(),
                )
            ],
            headers="keys",
        ),
    )


@main.command()
@json_flag
@ids_argument
def policy(
    json,
    ids,
):
    graph = GraphClient()
    objs = graph.device_management.configuration.get_policy(*ids)

    if json:
        print(
            orjson.dumps(
                [obj for obj in objs],
                option=orjson.OPT_INDENT_2,
            ).decode("utf-8"),
        )
        return

    print(
        tabulate(
            [
                {
                    "id": obj.id,
                    "name": obj.name,
                }
                for obj in sorted(
                    objs,
                    key=lambda obj: obj.name,
                )
            ],
            headers="keys",
        ),
    )


@main.command()
@json_flag
@ids_argument
def policy_setting(
    json,
    ids,
):
    graph = GraphClient()
    objs = graph.device_management.configuration.get_policy_setting(
        *ids or [obj.id for obj in graph.device_management.configuration.get_policy()]
    )

    if json:
        print(
            orjson.dumps(
                [obj for obj in objs],
                option=orjson.OPT_INDENT_2,
            ).decode("utf-8"),
        )
        return

    print(
        tabulate(
            [
                {
                    "id": obj.id,
                }
                for obj in sorted(
                    objs,
                    key=lambda obj: obj.id,
                )
            ],
            headers="keys",
        ),
    )


@main.command()
@json_flag
@ids_argument
def policy_assignment(
    json,
    ids,
):
    graph = GraphClient()
    objs = graph.device_management.configuration.get_configuration_policy_assignment(
        *ids or [obj.id for obj in graph.device_management.configuration.get_policy()]
    )

    if json:
        print(
            orjson.dumps(
                [obj for obj in objs],
                option=orjson.OPT_INDENT_2,
            ).decode("utf-8"),
        )
        return

    print(
        tabulate(
            [
                {"id": obj.id}
                for obj in sorted(
                    objs,
                    key=lambda obj: obj.id,
                )
            ],
            headers="keys",
        ),
    )


@main.command()
@json_flag
@ids_argument
def setting(
    json,
    ids,
):
    graph = GraphClient()
    objs = graph.device_management.configuration.get_configuration_setting(*ids)

    if json:
        print(
            orjson.dumps(
                [obj for obj in objs],
                option=orjson.OPT_INDENT_2,
            ).decode("utf-8"),
        )
        return

    print(
        tabulate(
            [
                {
                    "id": obj.id,
                    "name": obj.name,
                }
                for obj in sorted(
                    objs,
                    key=lambda obj: obj.name,
                )
            ],
            headers="keys",
        ),
    )


@main.command
@ids_argument
def xlsx(
    ids,
):
    graph = GraphClient()

    configuration_policies = graph.device_management.configuration.get_policy(*ids)
    configuration_policy_settings = (
        graph.device_management.configuration.get_policy_setting(*ids)
    )
    setting_definition_ids = {
        setting.settingInstance.settingDefinitionId
        for setting in configuration_policy_settings
    }

    table = sorted(
        [
            {
                "Category": str(
                    one(
                        graph.device_management.configuration.get_configuration_category(
                            one(
                                graph.device_management.configuration.get_configuration_setting(
                                    setting_definition_id
                                )
                            ).categoryId
                        )
                    )
                ),
                "Setting": {
                    "data": one(
                        graph.device_management.configuration.get_configuration_setting(
                            setting_definition_id
                        )
                    ).displayName
                },
                **{
                    policy.name: only(
                        [
                            {
                                "data": str(setting.settingInstance),
                            }
                            for setting in configuration_policy_settings
                            if setting.policyId == policy.id
                            and setting.settingInstance.settingDefinitionId
                            == setting_definition_id
                        ],
                        {
                            "data": "Not configured",
                        },
                    )
                    for policy in configuration_policies
                },
            }
            for setting_definition_id in setting_definition_ids
        ],
        key=lambda x: str(x["Category"]),
    )

    workbook = xlsxwriter.Workbook("policies.xlsx")
    worksheet = workbook.add_worksheet()
    category_format = workbook.add_format({"bold": True})
    row = 0

    for col, header in enumerate(
        ["Setting", *[policy.name for policy in configuration_policies]]
    ):
        worksheet.write(row, col, header)
    worksheet.freeze_panes(1, 0)

    row += 1

    category = None

    for data in table:
        if category != data["Category"]:
            category = data["Category"]
            worksheet.merge_range(
                row, 0, row, len(list(data.values())) - 2, category, category_format
            )
            row += 1
        for col, value in enumerate(list(data.values())[1:]):
            worksheet.write(row, col, value.get("data"), value.get("format", None))
        row += 1

    workbook.close()


if __name__ == "__main__":
    main()
