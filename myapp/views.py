from django.shortcuts import render
from django.http import HttpRequest

def dashboard_view(request: HttpRequest):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'myapp/dashboard/dashboard.html')
    return render(request, 'myapp/index.html')  # fallback for direct access

def manage_records_view(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'myapp/tables/table.html')
    return render(request, 'myapp/index.html')

def add_activity_form_view(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'myapp/forms/forms.html')
    return render(request, 'myapp/index.html')

def edit_activity_form_view(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'myapp/forms/edit_form.html')
    return render(request, 'myapp/index.html')

