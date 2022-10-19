from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.passwords.servicies.get_random_password import faker_password


from webargs import fields
from webargs.djangoparser import use_args


@use_args({"amount": fields.Int(missing=20)}, location="query")
def random_password(request: HttpRequest, args) -> HttpResponse:
    amount = args["amount"]
    return render(
        request,
        "random_pass.html",
        {
            "random_password": faker_password(amount=amount),
            "title": "Passwords",
        },
    )
