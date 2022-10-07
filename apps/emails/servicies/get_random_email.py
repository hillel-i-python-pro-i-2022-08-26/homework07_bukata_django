from faker import Faker

fake = Faker()


def faker_email():
    emails = []
    for i in range(10):
        email = fake.unique.email()
        emails.append(email)
    return emails
