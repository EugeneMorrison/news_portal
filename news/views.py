from django.views.generic import ListView, DetailView
from .models import Post

class NewsList(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']  # от новых к старым

class NewsDetail(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'post'