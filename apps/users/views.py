from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.users.services import generate_fake_users


# Create your views here.
def get_users(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "random_login.html",
        {"users": generate_fake_users()},
    )
