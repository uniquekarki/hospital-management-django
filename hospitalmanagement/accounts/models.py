from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

class Appointments(models.Model):
    patient_name = models.CharField(max_length=100)
    doctor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    reason = models.CharField(max_length=200, null=True)

