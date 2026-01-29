from django.urls import path, include
from index import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
]
