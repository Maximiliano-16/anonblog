from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели в интерфейсе админки."""

    list_display = ('pk', 'title', 'pub_date', 'author', 'body',)
    search_fields = ('title',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
