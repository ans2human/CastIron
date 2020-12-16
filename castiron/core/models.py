from django.db import models
# Create your models here.

Designation_choices = (
    ("SDE", "SOFTWARE DEVELOPMENT ENGINEER"),
    ("SSE", "SENIOR SOFTWARE ENGINEER"),
    
)

class Employee(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    designation = models.CharField(max_length=10, choices=Designation_choices, blank=True, null=True)
    isActive = models.BooleanField(default=True)

# +91