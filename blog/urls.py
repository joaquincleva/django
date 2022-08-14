from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("write/", views.write, name="write"),
    path("insert/", views.insert, name="insert"),
    path("post/<int:id>", views.post, name="post")
]