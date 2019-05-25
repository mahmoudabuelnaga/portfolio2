from django.db import models

# Create your models here.
class MyData(models.Model):
    name   = models.CharField(max_length=100)
    skills = models.CharField(max_length=300)
    img    = models.ImageField(upload_to='myphoto/')

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    img     = models.ImageField(upload_to='protfolio_img/')
    name    = models.CharField(max_length=300)
    summary = models.TextField()
    link    = models.URLField()

    def __str__(self):
        return self.name

class About(models.Model):
    cv = models.FileField(upload_to='cv/')
