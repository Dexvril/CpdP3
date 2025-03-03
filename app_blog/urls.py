from django.urls import path
from django.shortcuts import redirect
from app_blog.views.create import create
from app_blog.views.read import read_view
from app_blog.views.list_post import list_post_view
from app_blog.views.delete import delete_post

urlpatterns = [
    path("", lambda request: redirect("blog_list")),  # Redirect dari /blog/ ke /blog/list/
    path("create/", create, name="blog_create"),
    path("read/<int:id>/", read_view, name="blog_read"),
    path("list/", list_post_view, name="blog_list"),
    path("delete/<int:id>/", delete_post, name="blog_delete"),
]
