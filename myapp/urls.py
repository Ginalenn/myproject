from django.urls import path
from . import views
app_name = 'myapp'

urlpatterns = [
    path('', views.dashboard_view, name='manage_dashboard'),  # Home
    path('records/', views.manage_records_view, name='manage_records'),
    path('add-activity/', views.add_activity_form_view, name='add_activity_form'),
    path('edit-activity/', views.edit_activity_form_view, name='edit_activity_form'),
    path('activity/<int:pk>/', views.view_activity_view, name='view_activity'),
]



