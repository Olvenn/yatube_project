from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()


class Group (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    rules = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='group',
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.id)
