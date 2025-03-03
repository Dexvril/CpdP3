from django.shortcuts import render
from app_blog.utility import query  # Pastikan ini benar

def read_view(request, id):
    result = query("SELECT * FROM blog_post WHERE id = %s", [id])
    if not result:
        return render(request, "app_blog/read.html", {"error": "Post tidak ditemukan"})
    return render(request, "app_blog/read.html", {"post": result[0]})
