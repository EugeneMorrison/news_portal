from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django_filters.views import FilterView
from .models import Post, Comment, Author
from .filters import PostFilter
from .forms import PostForm, NewsForm, CommentForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.urls import reverse

def is_author(user):
    return user.groups.filter(name='authors').exists()

class NewsList(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset

        params = self.request.GET.copy()
        if 'page' in params:
            params.pop('page')
        context['query_params'] = params.urlencode()
        return context

class NewsDetail(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = Comment.objects.filter(post=post).order_by('-created_at')
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('news_detail', pk=post.pk)
        context = self.get_context_data()
        context['comment_form'] = form
        return self.render_to_response(context)


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news/post_form.html'
    success_url = reverse_lazy('news_list')
    permission_required = ['news.add_post', 'news.view_post']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user.author  # автор текущего пользователя

        # Автозаполнение post_type на основе URL
        if 'news' in self.request.path:
            post.post_type = 'NW'
        elif 'articles' in self.request.path:
            post.post_type = 'AR'

        post.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'post_type', 'categories']
    template_name = 'news/post_edit.html'
    success_url = reverse_lazy('news_list')
    permission_required = 'news.change_post'

    def get_success_url(self):
        return reverse('news_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news_list')
    permission_required = 'news.delete_post'

class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'news.add_post'  # право на создание поста
    form_class = NewsForm
    model = Post
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        form.instance.post_type = 'NW'
        form.instance.author = Author.objects.get(user=self.request.user)
        return super().form_valid(form)
        # post = form.save(commit=False)
        # post.post_type = 'news'
        # # Здесь можно добавить автора, если нужно
        # post.save()
        # return super().form_valid(form)