from rest_framework import serializers
from .models import imageupload

class imageuploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = imageupload
        fields= (
            'title',
            'images'
        )