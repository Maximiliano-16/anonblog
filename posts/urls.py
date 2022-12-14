from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('posts/<int:post_id>/comment/',
         views.add_comment,
         name='add_comment'),
    path('posts/<int:post_id>/like/', views.like_post, name='like_post'),
    path(
        'posts/<int:post_id>/dislike/',
        views.dislike_post, name='dislike_post'),
    # path('posts/<int:post_id>/like/', views.post_detail, name='post_detail'),
    # path('posts/<int:post_id>/unlike/', views.post_detail, name='post_detail'),
]
