from django.db import models
from django.core.validators import RegexValidator
from app.models import Host
from django.utils import timezone

# Create your models here.
phone_regex = RegexValidator(regex=r'^\+?9?1?\d{10}')

class VisitorProfileInfo(models.Model):

    username = models.CharField(max_length= 50, primary_key= True)
    email = models.EmailField(blank= False)
    name = models.CharField(max_length= 50, blank=False)
    phone = models.CharField(validators=[phone_regex], max_length=13, blank=False)
    address = models.CharField(max_length=256, blank=False)
    password = models.CharField(max_length = 50,blank = False)

    def __str__(self):
        return self.username

class RegisteredVisitorEntry(models.Model):

    username = models.ForeignKey(VisitorProfileInfo,on_delete= models.CASCADE)
    host = models.ForeignKey(Host, on_delete = models.CASCADE)
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()
    time_stamp = models.DateTimeField()

    def save(self):
        self.time_stamp = timezone.now()
        return super(RegisteredVisitorEntry, self).save()
        

    def __str__(self):
        return self.username.username
