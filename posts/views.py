from django.shortcuts import render
from posts.models import Post

# Create your views here.

def post_list_view(request):
    posts_query_set = Post.objects.all()
    context = {
        "object_list": posts_query_set,
    }
    return render(request, "posts/list.html", context=context)

def post_create_view(request):
    context = {}
    if request.method == "POST":
        post_obj = Post.objects.create(title=request.POST.get("title"),
                            content=request.POST.get("content"))
        context["object"] = post_obj
        context["created"] = True

    return render(request, "posts/create.html", context=context)

def post_detail_view(request, id=None):
    post_obj = None
    if id is not None:
        post_obj = Post.objects.get(id=id)
    context = {
        "object": post_obj,
    }
    return render(request, "posts/detail.html", context=context)