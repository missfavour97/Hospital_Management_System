from django import forms
from .models import Patient, Doctor

class PatientForm(forms.ModelForm): 
    class Meta: 
        model = Patient 
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth', 'phone', 'email', 'address']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'specialty', 'phone', 'email']