from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.members, name='members'),
]