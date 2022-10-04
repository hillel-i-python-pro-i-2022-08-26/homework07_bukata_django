from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.base.servicies.get_random_name import faker_name


def say_hi(request: HttpRequest, name=None) -> HttpResponse:
    if name is None:
        name = faker_name()
    return HttpResponse(f"Hello {name}, welcome")


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def random_mes(request: HttpRequest) -> HttpResponse:
    return render(request, "random_message.html", {"random_message": faker_name()})
