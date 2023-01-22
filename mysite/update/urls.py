from django.urls import path
from . import views

urlpatterns = [
    path('', views.update, name='update'),
    path('upload', views.upload, name='upload'),
    path('index', views.index, name='index')
]