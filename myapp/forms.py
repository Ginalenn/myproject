from django import forms
from .models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        # List all fields from the model that you want in the form
        fields = [
            'strategy_name', 'date_from', 'date_to',
            'activity_title', 'description',
            'funding_agency', 'implementing_agency', 'collaborating_agency',
            'sponsored_by', 'facilitated_by', 'participants',
            'proof_image'
        ]
        # Optional: Customize widgets, like making date fields use the date picker
        widgets = {
            'date_from': forms.DateInput(attrs={'type': 'date'}),
            'date_to': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        """
        Add Bootstrap's 'form-control' class and placeholders to each field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'strategy_name': 'e.g. Youth Empowerment Program',
            'activity_title': 'e.g. Barangay Cleanup Drive',
            'description': 'Describe the activity...',
            'funding_agency': 'Funding Agency',
            'implementing_agency': 'Implementing Agency',
            'collaborating_agency': 'Collaborating Agency',
            'sponsored_by': 'Sponsored By',
            'facilitated_by': 'Facilitated By',
            'participants': 'e.g. 50 Barangay Youth',
        }
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[field_name]