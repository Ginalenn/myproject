# myapp/models.py
from django.db import models
from django.conf import settings

class Strategy(models.Model):
    # ... your Strategy model ...
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Activity(models.Model):
    # Core fields from the form
    strategy_name = models.CharField(max_length=255) # Assuming text for simplicity
    date_from = models.DateField()
    date_to = models.DateField()
    activity_title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    # Agency & Participant fields
    funding_agency = models.CharField(max_length=200, blank=True)
    implementing_agency = models.CharField(max_length=200, blank=True)
    collaborating_agency = models.CharField(max_length=200, blank=True)
    sponsored_by = models.CharField(max_length=200, blank=True)
    facilitated_by = models.CharField(max_length=200, blank=True)
    participants = models.TextField(blank=True, help_text="List of participants, comma-separated or similar.")

    # Upload field
    proof_image = models.ImageField(upload_to='proofs/', blank=True, null=True)

    # Other relevant fields
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity_title