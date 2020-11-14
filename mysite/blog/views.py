from django.views import generic
# from django.shortcuts import render, get_object_or_404

from .models import Post


class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.all().order_by('-pub_date')


class PostDetailsView(generic.DetailView):
    model = Post
    template_name = "blog/post_details.html"

# TODO: increment `views`