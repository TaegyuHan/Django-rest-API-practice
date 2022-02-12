from django.urls import path
from .views import article_list, article_detail
from .views import ArticleAPIView, ArticleDetailAPIView


urlpatterns = [
    # path('article/', article_list), # 함수 버전
    # path('detail/<int:id>', article_detail), # 함수 버전

    path('article/', ArticleAPIView.as_view()), # 클래스 버전
    path('detail/<int:id>', ArticleDetailAPIView.as_view()), # 클래스 버전

]