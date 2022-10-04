from faker import Faker
import random
from collections.abc import Iterator
from apps.users.models import User

fake = Faker()


def get_user() -> User:
    return User(
        name=fake.unique.user_name(), text=fake.word(), num=random.randint(10, 100)
    )


def generate_fake_users(amount: int = 10) -> Iterator[User]:
    for _ in range(amount):
        return get_user()
