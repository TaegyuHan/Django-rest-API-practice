from django.urls import path, include
from .views import Imageuploadviewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'imageupload', Imageuploadviewset)

urlpatterns = [
    path('imageupload', include(router.urls)),
    path('', include(router.urls)),
]