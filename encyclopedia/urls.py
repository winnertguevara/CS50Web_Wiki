from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<title>", views.page_title, name="title"),
    path("wiki/", views.search, name="search"),
    path("create_page", views.new, name="new"),
    path("edit_page/<title>", views.edit, name="edit"),
    path("random", views.random_page, name="random"),
]