from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('add-doctor/', views.add_doctor, name='add_doctor'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('departments/', views.department_list, name='department_list'),
    path('prescriptions/', views.prescription_list, name='prescription_list'),
    path('add-appointment/', views.add_appointment, name='add_appointment'),
    path('add-department/', views.add_department, name='add_department'),
    path('add-prescription/', views.add_prescription, name='add_prescription'),
]