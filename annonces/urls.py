from django.urls import path
from annonces import views

urlpatterns = [
    path('', views.base, name='base'),
]