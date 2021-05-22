from django.urls import path
from sixyards import views

urlpatterns = [
    path('', views.home, name='home')
]
