from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(default='media/default_image.jpeg')

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

class UploadImageTest(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)

class Awsimage(models.Model):
    title = models.CharField(max_length=50)
    images = models.ImageField(upload_to="images/")