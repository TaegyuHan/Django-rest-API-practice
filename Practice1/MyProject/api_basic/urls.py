from django.urls import path, include
# from .views import article_list, article_detail # 함수 사용
from .views import (
    ArticleAPIView, ArticleDetailAPIView,
    GenericAPIView, ArticleViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),

    # path('article/', article_list), # 함수 버전
    # path('detail/<int:id>', article_detail),

    path('article/', ArticleAPIView.as_view()), # 클래스 버전
    path('detail/<int:id>/', ArticleDetailAPIView.as_view()),

    path('generic/article/<int:id>', GenericAPIView.as_view()),
]