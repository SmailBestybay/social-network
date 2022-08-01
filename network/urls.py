
from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    # path("make_post", views.make_post, name="make_post"),
    path("get_posts", views.get_posts, name="get_posts")
]
