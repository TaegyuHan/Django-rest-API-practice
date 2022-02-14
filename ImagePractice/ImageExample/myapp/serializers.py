from rest_framework import serializers
from .models import Person
from .models import UploadImageTest
from .models import Awsimage

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'image')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImageTest
        fields = ('name', 'image')


class AwsimageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awsimage
        fields = ('Title', 'images')