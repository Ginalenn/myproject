# myapp/views.py

# --- Core Django and Python Imports ---
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# --- Your App's Imports ---
from .models import Activity, Strategy # Import all necessary models
from .forms import ActivityForm       # Import your Django form

from django.contrib.auth.decorators import login_required

# ==============================================================================
# MAIN PAGE VIEWS
# Each view is responsible for rendering a complete page that extends base.html
# ==============================================================================

def dashboard_view(request):
    """
    Renders the main dashboard page.
    Gathers all necessary stats and chart data for display.
    """
    # In a real application, you would query your database here for these stats.
    dashboard_stats = {
        'total_activities': Activity.objects.count(),
        'average_impact': 82, # Placeholder, calculate as needed
        'active_strategies': Strategy.objects.count(), # Example
    }

    # Data for the charts
    activity_chart_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    activity_chart_data = [12, 19, 25, 30, 28, 35]
    strategy_chart_labels = ['Marketing', 'Analytics', 'Development', 'Sales', 'R&D']
    strategy_chart_data = [40, 25, 15, 10, 10]
    
    context = {
        **dashboard_stats, 
        'activity_chart_labels': json.dumps(activity_chart_labels),
        'activity_chart_data': json.dumps(activity_chart_data),
        'strategy_chart_labels': json.dumps(strategy_chart_labels),
        'strategy_chart_data': json.dumps(strategy_chart_data),
    }
    
    # Renders the full dashboard page, which should extend base.html
    return render(request, 'myapp/dashboard/dashboard.html', context)



def manage_records_view(request):
    """
    Renders the "Manage Records" page with the filterable table.
    """
    # Use select_related to optimize the query by fetching user data in one go
    activities = Activity.objects.select_related('created_by').all().order_by('-id')

    # Get distinct values for the filter panel dropdowns
    distinct_strategies = Activity.objects.order_by('strategy_name').values_list('strategy_name', flat=True).distinct()
    distinct_funders = Activity.objects.filter(funding_agency__isnull=False).exclude(funding_agency__exact='').order_by('funding_agency').values_list('funding_agency', flat=True).distinct()

    context = {
        'activities': activities,
        'distinct_strategies': distinct_strategies,
        'distinct_funders': distinct_funders,
    }
    
    # Renders the full "Manage Records" page, which extends base.html
    return render(request, 'myapp/tables/table.html', context)



def add_activity_form_view(request):
    """
    Handles displaying the blank "Add Activity" form (on GET request)
    and processing the submitted form data (on POST request).
    """
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES) # request.FILES for image uploads
        if form.is_valid():
            activity = form.save(commit=False)
            activity.created_by = request.user # Assign the logged-in user
            activity.save()
            
            messages.success(request, 'Activity report submitted successfully!')
            
            # Redirect to the main records page after a successful submission
            return redirect('myapp:manage_records')
    else:
        # If it's a GET request, just create a blank instance of the form
        form = ActivityForm()
    
    context = {'form': form}
    # Renders the full page containing the form
    return render(request, 'myapp/forms/forms.html', context)


    """
    Handles editing an existing activity, identified by its primary key (pk).
    """
    activity_instance = get_object_or_404(Activity, pk=pk)
    
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES, instance=activity_instance)
        if form.is_valid():
            form.save()
            messages.success(request, f'Activity "{activity_instance.activity_title}" was updated successfully!')
            return redirect('myapp:manage_records')
    else:
        # On GET, create a form pre-filled with the existing activity's data
        form = ActivityForm(instance=activity_instance)

    context = {
        'form': form,
        'activity': activity_instance # Pass instance for context (e.g., to show the title)
    }
    # Using a dedicated template for editing is good practice
    return render(request, 'myapp/forms/edit_form.html', context)




def view_activity_view(request, pk):
    """
    Renders a read-only detail page for a single activity.
    """
    # get_object_or_404 is a shortcut to get an object or raise a 404 error if not found
    activity = get_object_or_404(Activity, pk=pk)
    context = {'activity': activity}
    
    # We will create this new template file in the next step
    return render(request, 'myapp/details/view_detail.html', context)


def edit_activity_form_view(request, pk):
    """
    Handles both displaying and processing the form to edit an existing activity.
    """
    activity_instance = get_object_or_404(Activity, pk=pk)
    
    if request.method == 'POST':
        # Pass the instance to the form to update the existing object
        form = ActivityForm(request.POST, request.FILES, instance=activity_instance)
        if form.is_valid():
            form.save()
            messages.success(request, f'Activity "{activity_instance.activity_title}" was updated successfully!')
            return redirect('myapp:manage_records')
    else:
        # For a GET request, create a form pre-filled with the existing data
        form = ActivityForm(instance=activity_instance)

    context = {
        'form': form,
        'activity': activity_instance # Pass the object itself for context in the template
    }
    
    # We will create this new template file in the next step
    return render(request, 'myapp/forms/edit_form.html', context)