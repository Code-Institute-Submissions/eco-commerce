from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    image = models.ImageField(upload_to='images')
    headline = models.CharField(max_length=50, default='')
    author = models.CharField(max_length=50, default='')
    blog_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline
