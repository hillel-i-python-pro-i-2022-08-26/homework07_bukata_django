from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.passwords.servicies.get_random_password import faker_password


def random_password(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "random_pass.html",
        {
            "random_password": faker_password(),
            "title": "Passwords",
        },
    )
