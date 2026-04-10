from django.contrib import admin 
from .models import Patient, Doctor, Department, Appointment, Prescription

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Appointment)
admin.site.register(Prescription)