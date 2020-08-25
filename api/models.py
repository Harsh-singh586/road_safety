from django.db import models

# Create your models here.

class data(models.Model):
      url = models.CharField(max_length = 20)
      date_time = models.CharField(max_length = 50)
      
      def __str__(self):
          return self.url     
