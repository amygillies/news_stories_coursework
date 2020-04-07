from django.db import models


# Create your models here.
class Story(models.Model):
    heading = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name_plural = 'Stories'
