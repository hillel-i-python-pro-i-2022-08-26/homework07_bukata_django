from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.user_data_generator.services import generate_faker_user_data


# Create your views here.
def get_data(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "data.html",
        {"data": generate_faker_user_data()},
    )
