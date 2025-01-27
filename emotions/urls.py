from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_affirmations, name='get_affirmations'),
]
