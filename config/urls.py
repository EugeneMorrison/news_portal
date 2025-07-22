from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('news/', include('news.urls')),  # включаем все маршруты news через include()
    path('pages/', include('django.contrib.flatpages.urls')),# flatpages — отдельно
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]