from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('single_test/', views.single_test, name='single_test'),
    path('single_result/', views.single_result, name = 'single_result'),
    path('db_test/', views.db_test, name = 'db_test'),
    path('db_result/', views.db_result, name = 'db_result'),
]