from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    brief_description = models.TextField()
    body = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_published",)


class Comment(models.Model):
    # Connect comment with post using the ForeignKey and when post is deleted, the comments get removed as well.
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
