from django.shortcuts import get_object_or_404, redirect, render


def index(request):
    # post_list = Post.objects.select_related('author', 'group').all()
    # paginator = Paginator(post_list, posts_per_page)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {

    }
    return render(request, 'posts/index.html', context)


def post_detail(request, post_id):
    context = {

    }
    return render(request, 'posts/post_detail.html', context)
