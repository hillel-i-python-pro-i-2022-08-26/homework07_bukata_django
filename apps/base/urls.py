from django.urls import path
from . import views

app_name = "base_hello"
# urlpatterns = [
#    path("", views.say_hi, name="say_hi"),
# ]
# here we call function as an object, we give name for this path

# urlpatterns = [
#    path("", views.index, name="index"),
# ]
# path for index view

urlpatterns = [
    path("", views.random_mes, name="random_mes"),
]
