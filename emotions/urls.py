from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('affirmations/', views.get_affirmations, name='affirmations_list'),
    # Add other routes here
]
