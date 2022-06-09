from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:TITLE>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path('randompage', views.randompage, name="randompage"),
    path('newpage', views.newpage, name='newpage')
]