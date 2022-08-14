from django.db import models
import datetime

class Survey(models.Model):
    last_name=models.CharField(max_length=200,default="")
    name=models.CharField(max_length=200,default="")
    subject=models.CharField(max_length=200,default="")
    subject_grade=models.CharField(max_length=200,default="")
    weight=models.CharField(max_length=200,default="")
    height=models.CharField(max_length=200,default="")
    age=models.IntegerField(default=0)
    birthdate=models.DateField( default=datetime.date.today)
    city=models.CharField(max_length=200,default="Tunja")
    lives_with=models.CharField(max_length=200,default="")
    phisical_act=models.CharField(max_length=200,default="")
    sleep_hours=models.CharField(max_length=200,default="")
    extra_act=models.CharField(max_length=200,default="")
    
    def __str__(self):
        return self.name
    