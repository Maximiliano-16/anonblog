from django import forms
from django.contrib.auth import get_user_model

from .models import Post

User = get_user_model()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        labels = {
            'title': 'Заголовок',
            'body': 'Пост',
        }
        help_texts = {
            'title': 'Заголовок поста',
            'body': 'Текст поста',
        }
