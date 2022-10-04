from faker import Faker

fake = Faker()


def faker_name():
    return f"Hello, {fake.first_name()} wellcome"
