from sqlalchemy.orm import Session
from faker import Faker
from invoke import task

from app.config import Settings, get_settings
import app.models as m

fake = Faker()


NUM_TEST_USERS = 1000
NUM_TEST_POSTS = 1000


settings: Settings = get_settings()


@task
def fill_test_data(db: Session):
    # generate random users
    for _ in range(NUM_TEST_USERS):
        user = m.User(
            username=fake.unique.user_name(),
            email=fake.unique.email(),
            password=fake.password(),
        )
        db.add(user)
        db.commit()
        db.refresh(user)


# generate random posts
