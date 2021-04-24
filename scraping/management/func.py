from django.db import models
from django.utils import timezone


class data(models.model):
    
    
    def create(self,data):
        for i in data:
            i 




class Job(models.Model):
    date = models.CharField(max_length=30)
    taux = models.CharField(max_length=30)
    volume = models.CharField(max_length=30)
    encours = models.CharField(max_length=30)
    
    def __str__(self):
        return self.date
    class Meta:
        ordering = ['date']
    class Admin:
        pass

