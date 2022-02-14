from django.urls import path, include
from .views import ImageViewSet, AwsimageViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("wsimage", AwsimageViewSet)

urlpatterns = [
    path('upload/', ImageViewSet.as_view(), name='upload'),
    path('', include(router.urls)),
]