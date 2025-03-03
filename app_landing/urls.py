from django.urls import path
from .views import create_view, read_view, list_post_view

urlpatterns = [
    path("create/", create_view, name="blog_create"),
    path("read/<int:id>/", read_view, name="blog_read"),
    path("list/", list_post_view, name="blog_list"),
]
