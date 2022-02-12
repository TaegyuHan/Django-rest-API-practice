from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__' # 전체 보여주기
        # fields = ('id', 'title', 'author', 'email') # 선택 보여주기
