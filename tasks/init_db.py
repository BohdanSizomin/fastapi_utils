from sqlalchemy.orm import Session
from invoke import task
from app.config import Settings, get_settings
from app.model import User

NUM_TEST_USERS = 10
NUM_TEST_POSTS = 3


settings: Settings = get_settings()


@task
def fill_test_data(db: Session):
    from app.model import Post

    for uid in range(NUM_TEST_USERS):
        user = User(username=f"User{uid}", password="pa$$", email=f"user{uid}@test.com")
        db.add(user)
        db.commit()
        db.refresh(user)
        for pid in range(NUM_TEST_POSTS):
            db.add(
                Post(
                    title=f"Title{pid}",
                    content=(f"Test of post {pid}" * (pid + 1)),
                    user=user,
                )
            )
