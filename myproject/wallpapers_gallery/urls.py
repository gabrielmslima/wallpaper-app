from django.urls import path
from .views import wallpapers_view

urlpatterns = [
    path('', wallpapers_view, name='wallpapers'),
]