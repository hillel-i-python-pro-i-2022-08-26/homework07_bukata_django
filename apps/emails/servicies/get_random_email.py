from faker import Faker

fake = Faker()


def faker_email():
    email_list = []
    for i in range(10):
        email = fake.unique.email()
        email_list.append(email)
    return email_list
