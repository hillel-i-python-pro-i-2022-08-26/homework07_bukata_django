from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.user_data_generator.services import generate_faker_user_data


from webargs import fields
from webargs.djangoparser import use_args


@use_args({"amount": fields.Int(missing=20)}, location="query")
def get_data(request: HttpRequest, args) -> HttpResponse:
    amount = args["amount"]
    return render(
        request,
        "data.html",
        {
            "data": generate_faker_user_data(amount=amount),
            "title": "General users data",
        },
    )
