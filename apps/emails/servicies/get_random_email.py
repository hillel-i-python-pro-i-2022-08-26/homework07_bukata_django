from faker import Faker

fake = Faker()


def faker_email(amount: int):
    emails = []
    for i in range(amount):
        email = fake.unique.email()
        emails.append(email)
    return emails
