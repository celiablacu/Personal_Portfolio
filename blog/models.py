from django.db import models

# Create your models here.
class Blog(models.Model):
    #Check Django documenations on Field
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
