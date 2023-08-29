from fastapi_filter.contrib.sqlalchemy import Filter

import app.model as m


class UserFilter(Filter):
    email: str | None
    username: str | None
    is_verified: bool | None

    order_by: list[str] = ["+email"]
    # search: Optional[str]

    class Constants(Filter.Constants):
        model = m.User
        search_model_fields = ["name"]
