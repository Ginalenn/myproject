from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'myapp'

urlpatterns = [
    path('', views.dashboard_view, name='manage_dashboard'),  # Home
    path('records/', views.manage_records_view, name='manage_records'),
    path('add-activity/', views.add_activity_form_view, name='add_activity_form'),
    path('edit-activity/', views.edit_activity_form_view, name='edit_activity_form'),
    path('activity/<int:pk>/', views.view_activity_view, name='view_activity'),
    
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True # If a user is already logged in, redirect them
    ), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(
        next_page='login' # Redirect to login page after logout
    ), name='logout'),
]




