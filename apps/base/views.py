from django.http import HttpRequest, HttpResponse

from apps.base.servicies.get_random_name import faker_name


def say_hi(request: HttpRequest, name=None) -> HttpResponse:
    if name is None:
        name = faker_name()
    return HttpResponse(f"Hello {name}, welcome")
