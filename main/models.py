from django.db import models


class Service(models.Model):
    photo = models.ImageField(upload_to='Service/')
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
