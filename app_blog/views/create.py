from django.shortcuts import render, redirect
from app_blog.utility import query

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')

        print("INSERTING:", title, content)  # Debugging

        # Simpan data ke database dan ambil ID yang baru dibuat
        result = query("INSERT INTO blog_post (title, content) VALUES (%s, %s) RETURNING id", [title, content])

        print("INSERT RESULT:", result)  # Debugging hasil query

        if result and len(result) > 0:  # Pastikan result tidak kosong
            post_id = result[0].get("id")  # Ambil ID dari hasil query
            if post_id:
                return redirect(f"/blog/read/{post_id}/")  # Redirect ke post yang baru dibuat
            else:
                print("ERROR: ID tidak ditemukan dalam hasil query")  # Debugging tambahan
        else:
            print("ERROR: Gagal insert ke database atau result kosong")  # Debug jika insert gagal

    return render(request, "app_blog/create.html")
