from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.users.module.services import generate_fake_users

from webargs import fields
from webargs.djangoparser import use_args


@use_args({"amount": fields.Int(missing=20)}, location="query")
def get_users(request: HttpRequest, args) -> HttpResponse:
    amount = args["amount"]
    return render(
        request,
        "random_login.html",
        {
            "users": generate_fake_users(amount=amount),
            "title": "Users",
        },
    )
