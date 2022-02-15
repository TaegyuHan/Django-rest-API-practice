from rest_framework import viewsets

from .models import imageupload
from .serializers import imageuploadSerializer

class Imageuploadviewset(viewsets.ModelViewSet):
   queryset = imageupload.objects.all()
   serializer_class = imageuploadSerializer