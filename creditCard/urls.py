from os import name
from django.urls import path
from numpy import nan
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('single_test/', views.single_test, name='single_test'),
    path('single_result/', views.single_result, name = 'single_result'),
    path('db_test/', views.db_test, name = 'db_test'),
    path('db_result/', views.db_result, name = 'db_result'),
    path('load_file/', views.load_file, name = 'load_file'),
    path('save_file/', views.save_file, name = 'save_file'),
    path('predict_file_data/', views.predict_file_data, name = 'predict_file_data'),
]