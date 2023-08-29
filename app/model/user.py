from sqlalchemy.orm import relationship

from app.database import db
from .base_user import BaseUser


class User(db.Model, BaseUser):
    posts = relationship("Post", viewonly=True)

    __tablename__ = "users"
