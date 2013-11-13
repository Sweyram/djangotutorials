from django.db import models

# Create your models here.
class todo(models.Model): #Table name, has to wrap models.Model to get the functionality of Django.  
          
    name = models.CharField(max_length=100, unique=True)  
    description = models.TextField() 
    created = models.DateTimeField()  
  
    def __unicode__(self):
        return self.name  