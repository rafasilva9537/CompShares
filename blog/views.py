from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.http import Http404

# Create your views here.
def home(request):
    posts = Post.objects.order_by("-id")[:6]
    return render(request, "blog/home.html", {"posts": posts})

def post(request, post_id):
    # TODO: find alternatives to not expose the post id
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/post.html", {"post": post})