from django.shortcuts import render, redirect
from .models import Patient, Doctor, Appointment, Prescription, Department
from .forms import PatientForm, DoctorForm

def home(request):
    return render(request, 'home.html')

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients.html', {'patients': patients})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'add_patient.html', {'form': form})

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors})

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'add_doctor.html', {'form': form})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments.html', {'appointments': appointments})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments.html', {'departments': departments})

def prescription_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'prescriptions.html', {'prescriptions': prescriptions})