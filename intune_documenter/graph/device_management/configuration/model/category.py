from functools import cached_property

from intune_documenter.graph_object import GraphObject

from more_itertools import one


class Category(GraphObject):
    def __init__(
        self,
        **kwargs,
    ):
        self.childCategoryIds = kwargs.pop("childCategoryIds")
        self.description = kwargs.pop("description")
        self.displayName = kwargs.pop("displayName")
        self.id = kwargs.pop("id")
        self.parentCategoryId = kwargs.pop("parentCategoryId")
        self.rootCategoryId = kwargs.pop("rootCategoryId")
        self.categoryDescription = (
            kwargs.pop("categoryDescription")
            if "categoryDescription" in kwargs
            else None
        )

        if "@odata.context" in kwargs:
            kwargs.pop("@odata.context")
        super().__init__(
            **kwargs,
        )

    @cached_property
    def has_parent(self):
        return (
            self.parentCategoryId
            and (self.parentCategoryId != self.id)
            and (self.parentCategoryId != "00000000-0000-0000-0000-000000000000")
        )

    @cached_property
    def tree(self):
        if self.has_parent:
            yield from one(
                self.client.get_configuration_category(
                    self.parentCategoryId,
                ),
            ).tree
        yield self

    @cached_property
    def path(self):
        return "\\".join([obj.displayName for obj in self.tree])

    def __str__(self):
        return self.path
