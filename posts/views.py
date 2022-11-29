from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .models import Post

posts_per_page = 10


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, posts_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }

    return render(request, 'posts/index.html', context)


def post_detail(request, post_id):
    context = {

    }
    return render(request, 'posts/post_detail.html', context)
