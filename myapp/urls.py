from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/', views.forms, name='forms'),
    path('table/', views.table, name='table'),
    path('add-activity/', views.add_activity_form, name='add_activity_form'),
    path('manage_records/', views.manage_records, name='manage_records'),
     path('dashboard/', views.dashboard, name='dashboard'),
]
