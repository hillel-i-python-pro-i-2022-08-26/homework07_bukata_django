from django.urls import path
from . import views

# we need it to dynamic creat routs without making links
app_name = "users"
# here we call function as an object, we give name for this path
# path for our view

urlpatterns = [
    path("", views.get_users, name="index"),
]
