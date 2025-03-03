# views/update.py
from django.shortcuts import render, redirect
from app_blog.utility import query

def update_post(request, id):
    # Ambil data post berdasarkan ID
    post = query("SELECT * FROM blog_post WHERE id = %s", [id])
    
    if not post:
        return render(request, "app_blog/not_found.html")
    
    post = post[0]  # Ambil post pertama (seharusnya hanya satu)
    
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        
        # Update data di database
        query("UPDATE blog_post SET title = %s, content = %s WHERE id = %s", [title, content, id])
        
        return redirect(f"/blog/read/{id}/")
    
    return render(request, "app_blog/update.html", {"post": post})
