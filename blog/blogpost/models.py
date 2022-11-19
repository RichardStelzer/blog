from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    brief_description = models.TextField()
    body = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_published",)

# class Comment(models.Model):
#    content = models.TextField()
#    author = models.CharField()
#    date_published = models.DateTimeField(auto_now_add=True)
