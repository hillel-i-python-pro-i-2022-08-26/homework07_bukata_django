from faker import Faker

fake = Faker()


def faker_password():
    password_list = []
    for _ in range(10):
        password = fake.unique.password()
        password_list.append(password)
    return password_list
