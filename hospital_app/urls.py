from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('add-doctor/', views.add_doctor, name='add_doctor'),
]