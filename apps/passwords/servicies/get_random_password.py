from faker import Faker

fake = Faker()


def faker_password(amount: int):
    password_list = []
    for _ in range(amount):
        password = fake.unique.password()
        password_list.append(password)
    return password_list
