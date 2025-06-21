from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='manage_dashboard'),  # Home
    path('records/', views.manage_records_view, name='manage_records'),
    path('add-activity/', views.add_activity_form_view, name='add_activity_form'),
    path('edit-activity/', views.edit_activity_form_view, name='edit_activity_form'),
]

