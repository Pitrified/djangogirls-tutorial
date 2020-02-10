from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Post


def post_list(request):
    the_post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    return render(request, "blog/post_list.html", {"posts": the_post_list})


def post_detail(request, pk):
    the_post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": the_post})
