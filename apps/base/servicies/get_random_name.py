from faker import Faker

fake = Faker()


def faker_name():
    return fake.first_name()
