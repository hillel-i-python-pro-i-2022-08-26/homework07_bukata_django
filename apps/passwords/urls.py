from django.urls import path
from . import views

app_name = "passwords"
# here we call function as an object, we give name for this path
# path for index view

urlpatterns = [
    path("", views.random_password, name="random_password"),
]
