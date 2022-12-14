import email
from pyexpat import model
from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.
# defines the database
class Contact(models.Model):
    name = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    phone = models.CharField(max_length = 12)
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name.lower()
 
class Rating(models.Model):
    name = models.CharField(max_length = 122)
    rating = models.CharField(max_length = 1)
    
    def __str__(self):
        return self.name.lower()
            
    