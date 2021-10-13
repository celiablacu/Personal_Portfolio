from django.db import models

# Create your models here -- classes

class Project(models.Model):
    #Check Django documenations on Field
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    internalurl = models.CharField(max_length=100,blank=True)
    github = models.URLField(blank=True)

    def __str__(self):
        return self.title
