from django.db import models


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    when = models.DateTimeField()




class Emails(models.Model):
    mails = models.EmailField()
    def __str__(self):
        return self.mails
