# myapp/forms.py
from django import forms
from .models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        # List all the fields from your model that you want in the form
        fields = [
            'strategy_name', 'date_from', 'date_to',
            'activity_title', 'description',
            'funding_agency', 'implementing_agency', 'collaborating_agency',
            'sponsored_by', 'facilitated_by', 'participants', 'proof_image'
        ]

        # Add Bootstrap classes to the form fields for styling using widgets
        widgets = {
            'strategy_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_from': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_to': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'activity_title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'funding_agency': forms.TextInput(attrs={'class': 'form-control'}),
            'implementing_agency': forms.TextInput(attrs={'class': 'form-control'}),
            'collaborating_agency': forms.TextInput(attrs={'class': 'form-control'}),
            'sponsored_by': forms.TextInput(attrs={'class': 'form-control'}),
            'facilitated_by': forms.TextInput(attrs={'class': 'form-control'}),
            'participants': forms.TextInput(attrs={'class': 'form-control'}),
            'proof_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }