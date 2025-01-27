from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("post/<int:post_id>", views.post, name="post"),
    path("home/", views.home, name="home"),
]