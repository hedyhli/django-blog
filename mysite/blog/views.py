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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['is_admin'] = user.is_staff or user.is_superuser
        return context


class PostDetailsView(generic.DetailView):
    model = Post
    template_name = "blog/post_details.html"

    def get(self, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        post.views = F('views') + 1
        post.save()
        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['is_admin'] = user.is_staff or user.is_superuser
        return context


def like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.likes = F("likes") + 1
    post.save()
    return HttpResponseRedirect(reverse('blog:post', args=(post.id,)))

# def index(request):
#     return "hi"