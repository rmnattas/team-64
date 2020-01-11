from django.db import models

# Create your models here.

class Record(models.Model):
    phrase = models.CharField(max_length=255)
    encryptedPhrase = models.CharField(max_length=255)
    requested = models.DateTimeField(auto_now_add=True)
