from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('sesshandl.urls')),
    path('polls/', include('polls.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
