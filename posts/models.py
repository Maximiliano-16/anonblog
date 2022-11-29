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

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']

