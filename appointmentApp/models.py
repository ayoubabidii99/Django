from django.db import models
from AccountApp.models import Doctor,Patient

# Create your models here.
class appointment(models.Model):
    reason = models.TextField()
    prescription= models.FileField(
        blank=True,
        upload_to='prescriptions/'
    )
    class Status (models.textChoices):
        PENDING = "PENDING" , "En attente"
        CONFIRMED="CONFIRMED" , "confirme"
        CANCELLED="CANCELLED" , "annulé"
    status = models.CharField(max_length=10 , choices=Status.Choices,default=Status.PENDING)
    duration_minutes= models.PositiveBigIntegeration(defaul=30)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    appointment_date= models.DateTimeField()
    doctor =models.ForeignKey(Doctor,on_delete=models.CASCADE , related_name="appointments")
    #patient =models.ForeignKey("AccountApp.patient" , on_delete=models.CASCADE , related_name="appointments")
    Patient =models.ForeignKey(Patient,on_delete=models.CASCADE , related_name="appointments")


