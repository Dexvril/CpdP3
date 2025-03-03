from django.shortcuts import redirect
from app_blog.utility import query

def delete_post(request, id):
    query("DELETE FROM blog_post WHERE id = %s", [id])  # Hapus post
    return redirect("/blog/list/")  # Redirect setelah penghapusan
