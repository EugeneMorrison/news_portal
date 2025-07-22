from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'post_type', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'categories': forms.CheckboxSelectMultiple(),
            'post_type': forms.Select(attrs={'class': 'form-control'}),
        }
class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['post_type', 'author', 'created_at', 'rating']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'categories': forms.CheckboxSelectMultiple(),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Введите комментарий'}),
        }
        labels = {
            'text': '',
        }
