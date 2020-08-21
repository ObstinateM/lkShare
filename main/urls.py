from django.urls import path
from . import views

urlpatterns = [
    path('', views.lkPage, name='lkEmpty'),
    path('<urlid>/', views.lkPage, name='lkFill'),
]