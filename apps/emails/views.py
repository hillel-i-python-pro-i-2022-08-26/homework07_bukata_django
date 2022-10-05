from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.emails.servicies.get_random_email import faker_email


def random_email(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "random_email.html",
        {
            "random_email": faker_email(),
            "title": "Emails",
        },
    )
