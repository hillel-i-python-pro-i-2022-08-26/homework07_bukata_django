from django.urls import path
from . import views

app_name = "emails"
# here we call function as an object, we give name for this path
# path for index view

urlpatterns = [
    path("", views.random_email, name="random_email"),
]
