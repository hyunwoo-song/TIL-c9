from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.TextField()
    
class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name='patients')   # , through='Reservation'


# Doctor: Reservation = 1:N   -> Reservation = N*Doctor
# Patient: Reservation = 1:M  -> Reservation = M*Patient
# Doctor: Patient = M:N       -> N*Doctor = M*Patient
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    
    