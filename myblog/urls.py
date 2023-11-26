from django.urls import path
from .views import index, add_post

urlpatterns = [
    path('', index, name='home'),
    path('add/', add_post, name='add'),
]
