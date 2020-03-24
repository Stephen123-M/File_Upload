from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Picture(models.Model):
    date = models.DateTimeField(auto_now_add = True)
    photo = models.ImageField(upload_to = 'uploads/')
    owner = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.name
    
                              
