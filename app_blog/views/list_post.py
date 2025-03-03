from django.shortcuts import render
from app_blog.utility import query  # Pastikan ini benar

def list_post_view(request):
    posts = query("SELECT * FROM blog_post ORDER BY id DESC")  # Ambil semua post
    return render(request, "app_blog/list_post.html", {"posts": posts})
