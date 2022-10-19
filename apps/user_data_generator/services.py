import json
from faker import Faker

fake = Faker()


def generate_faker_user_data(amount: int):
    return json.loads(
        fake.json(
            data_columns=[
                ("Username", "user_name"),
                ("Email", "email"),
                ("Password", "password"),
            ],
            num_rows=amount,
        )
    )
