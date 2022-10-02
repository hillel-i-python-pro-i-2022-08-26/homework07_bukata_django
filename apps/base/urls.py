from django.urls import path
from . import views

urlpatterns = [
    path("", views.say_hi, name="say_hi"),
]
# here we call function as an object, we give name for this path
