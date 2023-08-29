from pydantic import Field
from fastapi_filter import FilterDepends, with_prefix
from fastapi_filter.contrib.sqlalchemy import Filter

import app.model as m
import app.schema as s

from .user import UserFilter


class PostFilter(Filter):
    title: str | None = Field(alias="title")
    content: str | None = Field(alias="content")
    is_published: bool | None = Field(alias="is_published")
    publication_type__in: list[s.enums.PublicationType] | None = Field(
        alias="publication_type"
    )
    order_by: list[str] | None = ["-created_at"]  # default sort is by id
    user__email: str | None = FilterDepends(with_prefix("user", UserFilter))

    class Constants(Filter.Constants):
        model = m.Post

    class Config:
        allow_population_by_field_name = True
