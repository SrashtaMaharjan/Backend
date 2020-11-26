
from django.db import models


class mutual_table(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    donationPlatform = models.CharField(max_length=100)
    needLevel = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(max_length=1000)

   # def __str__(self):
    #    return self.name


#class Choice(models.Model):
 #   question = models.ForeignKey(Question, on_delete=models.CASCADE)
  
  #  choice_text = models.CharField(max_length=200)
   # votes = models.IntegerField(default=0)
