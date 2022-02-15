from django.db import models


def nameFile(instance, title):
    return '/'.join(['images', str(instance.title), title])


class imageupload(models.Model):
    title = models.CharField(max_length=50)
    images = models.ImageField(upload_to=nameFile)