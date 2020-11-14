from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    # /blog/
    path('', views.IndexView.as_view(), name='blog'),
    # /blog/post/1
    path('post/<int:pk>/', views.PostDetailsView.as_view(), name="post"),
    # /authors/
    # path('authors/', views.authors),
    # /author/1
    # path('author/<int:user_id>', views.author_details)
]