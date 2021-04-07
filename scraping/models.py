from django.db import models
from django.utils import timezone



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



class  Rule(models.Model):
    code = 'python manage.py scrape'
    was_executed_before = models.BooleanField(default=False) # it was not executed before.

    def execute(self):
        # omit return or leave it depending on your needs
        return eval(self.code)