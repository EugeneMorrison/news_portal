from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), #'django.contrib.auth.urls' - django form
    # path("accounts/", include("accounts.urls")),
    path('', include('news.urls')),
]
