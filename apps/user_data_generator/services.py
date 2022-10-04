import json
from faker import Faker

fake = Faker()


def generate_faker_user_data():
    return json.loads(
        fake.json(
            data_columns=[
                ("Username", "username"),
                ("Email", "email"),
                ("Password", "password"),
            ],
            num_rows=10,
        )
    )
