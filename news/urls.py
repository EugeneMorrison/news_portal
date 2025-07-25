from django.urls import path
from .views import (
    NewsList,
    NewsDetail,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    NewsCreate,
)

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),   # /news/
    path('search/', NewsList.as_view(), name='news_search'),          # /news/search/
    path('create/', NewsCreate.as_view(), name='news_create'),        # /news/create/
    path('articles/create/', NewsCreate.as_view(), name='news_create'), # /news/articles/create/
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),      # /news/1/
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'), # /news/1/edit/
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),# /news/1/delete/
    path('create/', PostCreateView.as_view(), name='post_create'),
]