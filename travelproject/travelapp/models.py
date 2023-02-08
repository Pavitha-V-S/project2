from django.db import models

# Create your models here.
class destinations(models.Model):
    Name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.Name
class team(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='imgs')
    def __str__(self):
        return self.name


