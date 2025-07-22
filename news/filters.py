from django_filters import FilterSet, DateFilter, ModelChoiceFilter, CharFilter
from django.forms import DateInput
from .models import Post, Category

class PostFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Название')

    category = ModelChoiceFilter(
        field_name='categories',  # связь ManyToMany или ForeignKey, проверь модель
        queryset=Category.objects.all(),
        label='Категория'
    )

    created_after = DateFilter(
        field_name='created_at',
        lookup_expr='gte',
        widget=DateInput(attrs={'type': 'date'}),
        label='Позже даты'
    )

    class Meta:
        model = Post
        fields = []
