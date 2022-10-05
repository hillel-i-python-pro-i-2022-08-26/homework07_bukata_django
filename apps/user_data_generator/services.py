import json
from faker import Faker

fake = Faker()


def generate_faker_user_data():
    return json.loads(
        fake.json(
            data_columns=[
                ("Username", "user_name"),
                ("Email", "email"),
                ("Password", "password"),
            ],
            num_rows=10,
        )
    )


print(generate_faker_user_data())
