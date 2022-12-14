from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .models import Post, Comment, Like, Dislike
from .forms import PostForm, CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST,
                        files=request.FILES or None,)
        if form.is_valid():
            commit = form.save(commit=False)
            commit.save()
            return redirect('posts:index')
        return render(request, 'posts/create_post.html', {'form': form})
    form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # is_liked = False
    # if post.likes.filter(id=request.user.id).exists():
    #     is_liked = True
    form = CommentForm(request.POST)
    comments = post.comments.all()

    context = {
        'post': post,
        'form': form,
        'comments': comments,
        # 'is_liked': is_liked,

    }
    return render(request, 'posts/post_detail.html', context)


def like_post(request, post_id):
    # user = request.user
    post = get_object_or_404(Post, id=post_id)
    current_likes = post.likes
    liked = Like.objects.filter(post=post).count()
    if not liked:
        liked = Like.objects.create(post=post)
        current_likes += 1
    else:
        liked = Like.objects.filter(post=post).delete()
        current_likes -= 1
    post.likes = current_likes
    post.save()
    return HttpResponseRedirect(reverse('posts:post_detail', args=[post_id]))


def dislike_post(request, post_id):
    # user = request.user
    post = get_object_or_404(Post, id=post_id)
    current_dislikes = post.dislikes
    disliked = Dislike.objects.filter(post=post).count()
    if not disliked:
        disliked = Dislike.objects.create(post=post)
        current_dislikes += 1
    else:
        disliked = Dislike.objects.filter(post=post).delete()
        current_dislikes -= 1
    post.dislikes = current_dislikes
    post.save()
    return HttpResponseRedirect(reverse('posts:post_detail', args=[post_id]))


def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('posts:post_detail', post_id=post_id)
