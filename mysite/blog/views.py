from django.views import generic
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import reverse

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


def like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.likes = F("likes") + 1
    post.save()
    return HttpResponseRedirect(reverse('blog:post', args=(post.id,)))

# def index(request):
#     return "hi"