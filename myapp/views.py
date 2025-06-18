from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import json # Make sure to import the json library

# --- Main Views for AJAX Content Loading ---

def dashboard_view(request: HttpRequest) -> HttpResponse:
 
    # This check ensures that only AJAX requests get the partial content.
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        
        # --- Prepare the context directly inside the view ---
        # In a real application, you would query your database here.
        dashboard_stats = {
            'total_activities': 124,
            'completed_activities': 98,
            'average_impact': 77,
            'active_strategies': 16,
        }

        # Data for the Activity Trends line chart
        activity_chart_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        activity_chart_data = [12, 19, 25, 30, 28, 35]

        # Data for the Strategy Usage doughnut chart
        strategy_chart_labels = ['Digital Marketing', 'Analytics', 'Development', 'Sales', 'R&D']
        strategy_chart_data = [40, 25, 15, 10, 10]
        
        context = {
            # Use the ** operator to unpack the stats dictionary into the context
            **dashboard_stats, 
            
            # Use json.dumps to safely convert Python lists into JS-readable arrays
            'activity_chart_labels': json.dumps(activity_chart_labels),
            'activity_chart_data': json.dumps(activity_chart_data),
            'strategy_chart_labels': json.dumps(strategy_chart_labels),
            'strategy_chart_data': json.dumps(strategy_chart_data),
        }
        # Render the partial template with the prepared context
        return render(request, 'myapp/dashboard/dashboard.html', context)

    # Fallback for direct access: load the main page which will then
    # use AJAX to load the dashboard content.
    return render(request, 'myapp/index.html')


def manage_records_view(request: HttpRequest) -> HttpResponse:
    """
    Handles requests for the 'Manage Records' table.
    - AJAX: Returns the 'table.html' partial.
    - Direct Load: Returns the main 'index.html' base template.
    """
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # You can pass context with your records here if needed
        # context = {'records': YourModel.objects.all()}
        return render(request, 'myapp/tables/table.html') #, context)
    return render(request, 'myapp/index.html')


def add_activity_form_view(request: HttpRequest) -> HttpResponse:
    """
    Handles requests for the 'Add New Record' form.
    - AJAX: Returns the 'forms.html' partial.
    - Direct Load: Returns the main 'index.html' base template.
    """
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # You can pass a Django form instance here
        # from .forms import ActivityForm
        # context = {'form': ActivityForm()}
        return render(request, 'myapp/forms/forms.html') #, context)
    return render(request, 'myapp/index.html')


def edit_activity_form_view(request: HttpRequest) -> HttpResponse:
    """
    Handles requests for the 'Edit Record' form.
    - AJAX: Returns the 'edit_form.html' partial.
    - Direct Load: Returns the main 'index.html' base template.
    """
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # This view would typically take an ID, e.g., edit_activity_form_view(request, pk)
        # instance = YourModel.objects.get(id=pk)
        # form = ActivityForm(instance=instance)
        # context = {'form': form}
        return render(request, 'myapp/forms/edit_form.html') #, context)
    return render(request, 'myapp/index.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ActivityForm # Import the form we just created

# Use @login_required to ensure a user is logged in before they can add an activity

def add_activity_form_view(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = ActivityForm(request.POST, request.FILES) # request.FILES is crucial for uploads
        if form.is_valid():
            # Don't save to DB yet, we need to add the user first
            activity = form.save(commit=False)
            activity.created_by = request.user # Assign the logged-in user
            activity.save() # Now save the instance to the database
            
            # Add a success message
            messages.success(request, 'Activity report submitted successfully!')
            
            # Redirect to the records page after a successful submission
            return redirect('manage_records')
    else:
        # If a GET request, create a blank form
        form = ActivityForm()
    
    # This context will be sent whether the form is blank (GET) or invalid (POST)
    context = {'form': form}
    return render(request, 'myapp/forms/forms.html', context)