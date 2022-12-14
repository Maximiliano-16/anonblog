from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    body = models.TextField()
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True
    )
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name='Комментарий',
        on_delete=models.CASCADE,
        null=True,
        related_name='comments',
    )

    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='user_like'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='post_like'
    )


class Dislike(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='user_dislike'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='post_dislike'
    )
