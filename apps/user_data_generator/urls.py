from django.urls import path
from . import views

app_name = "data"
urlpatterns = [
    path("", views.get_data, name="data"),
]
