from .models import *
from django.forms import ModelForm, TextInput

class AppointmentsForm(ModelForm):
    class Meta:
        model = Appointments
        fields = [
            'patient_name','patient_email','doctor','appointment_time','reason'
        ]