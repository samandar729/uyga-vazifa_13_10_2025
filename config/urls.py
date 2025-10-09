
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app111',include('app111.urls')),
    path('app222',include('app222.urls')),
    path('app333',include('app333.urls')),
]
