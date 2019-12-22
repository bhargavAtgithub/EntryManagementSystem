from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from django.utils import timezone
# Create your models here.

phone_regex = RegexValidator(regex=r'^\+?9?1?\d{10}')


class Host(models.Model):
    name = models.CharField(max_length=50, primary_key=True,)
    email = models.EmailField()
    phone = models.CharField(validators=[phone_regex], max_length=13)
    address = models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse("app:visitor_entry")

    def __str__(self):
        return self.name

class VisitorEntry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(validators=[phone_regex], max_length=13)
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()
    time_stamp = models.DateTimeField()
    host = models.ForeignKey(Host, on_delete = models.CASCADE )

    def save(self):

        self.time_stamp = timezone.now()
        return super(VisitorEntry, self).save()
        
    def get_absolute_url(self):
        return reverse("app:visitor_entry")

    def __str__(self):
        return self.name