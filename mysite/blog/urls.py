from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    # /blog/
    path('', views.IndexView.as_view(), name='blog'),
    # /blog/post/1
    path('post/<int:pk>/', views.PostDetailsView.as_view(), name="post"),
    # liking a post
    path('post/<int:pk>/like', views.like, name='like')
]