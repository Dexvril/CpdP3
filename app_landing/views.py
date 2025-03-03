from django.shortcuts import render

def create_view(request):
    return render(request, "create.html")

def read_view(request, id):
    return render(request, "read.html", {"id": id})

def list_post_view(request):
    return render(request, "list_post.html")
