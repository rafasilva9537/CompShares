from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("profile/", views.profile),
    path("login/", views.login)
]