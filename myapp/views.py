from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')

def forms(request):
    return render(request, 'myapp/forms.html')

def table(request):
    return render(request, 'myapp/table.html')

def add_activity_form(request):
    return render(request, 'myapp/forms.html')

def manage_records(request): 
    return render(request, 'myapp/table.html' )


def dashboard(request): 
    return render(request, 'myapp/dashboard.html' )