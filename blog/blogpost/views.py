from django.shortcuts import get_object_or_404, redirect, render

from .models import Post
from .forms import CommentForm


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)  # Gets form data and passes it to the CommentForm class

        if form.is_valid():
            comment = form.save(commit=False)  # Create temporary comment, does not submit to the database yet
            comment.post = post  # Add foreign key and connect comment to post by doing so
            comment.save()  # Submit comment to the database

            return redirect("post_detail", slug=slug)
    else:
        form = CommentForm()

    return render(request, "blogpost/detail.html", {"post": post, "form": form})
