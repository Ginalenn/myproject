from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    strategy_name = models.CharField(max_length=200)
    activity_title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField(blank=True, null=True)
    
    # Agency fields
    funding_agency = models.CharField(max_length=200, blank=True)
    implementing_agency = models.CharField(max_length=200, blank=True)
    collaborating_agency = models.CharField(max_length=200, blank=True)
    sponsored_by = models.CharField(max_length=200, blank=True)
    facilitated_by = models.CharField(max_length=200, blank=True)
    participants = models.CharField(max_length=255, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity_title



from django.contrib.auth.models import User

class Activity(models.Model):
    # ... (all your existing fields: strategy_name, activity_title, etc.)
    strategy_name = models.CharField(max_length=200)
    activity_title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField(blank=True, null=True)
    
    funding_agency = models.CharField(max_length=200, blank=True)
    implementing_agency = models.CharField(max_length=200, blank=True)
    collaborating_agency = models.CharField(max_length=200, blank=True)
    sponsored_by = models.CharField(max_length=200, blank=True)
    facilitated_by = models.CharField(max_length=200, blank=True)
    participants = models.CharField(max_length=255, blank=True)

    # NEW FIELD for the image upload
    proof_image = models.ImageField(upload_to='activity_proofs/', blank=True, null=True)
    
    # This should already be there
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity_title