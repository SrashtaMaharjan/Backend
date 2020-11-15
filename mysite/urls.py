from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('first_app/', include('first_app.urls')),
    path('admin.py/', admin.site.urls),
]