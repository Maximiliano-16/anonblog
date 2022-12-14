from django import forms
from django.contrib.auth import get_user_model

from .models import Post, Comment

User = get_user_model()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'image')
        labels = {
            'title': 'Заголовок',
            'body': 'Пост',
            'image': 'Картинка'
        }
        help_texts = {
            'title': 'Заголовок поста',
            'body': 'Текст поста',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            'text': 'Текст',

        }
        help_texts = {
            'text': 'Текст нового комментария',
        }

