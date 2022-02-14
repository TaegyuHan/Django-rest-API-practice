import json
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .models import UploadImageTest, Awsimage
from .serializers import ImageSerializer, AwsimageSerializer


class ImageViewSet(ListAPIView):
    queryset = UploadImageTest.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        # file = request.data['file']
        file = request.data
        image = UploadImageTest.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


class AwsimageViewSet(ModelViewSet):
    queryset = Awsimage.objects.all()
    serializer_class = AwsimageSerializer