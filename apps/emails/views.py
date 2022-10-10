from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.emails.servicies.get_random_email import faker_email

from webargs import fields
from webargs.djangoparser import use_args


@use_args({"amount": fields.Int(missing=20)}, location="query")
def random_email(request: HttpRequest, args) -> HttpResponse:
    amount = args["amount"]
    return render(
        request,
        "random_email.html",
        {
            "random_email": faker_email(amount=amount),
            "title": "Emails",
        },
    )
