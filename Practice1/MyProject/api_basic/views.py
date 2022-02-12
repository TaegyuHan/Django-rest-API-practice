from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser # json으로 보이기
from rest_framework.decorators import api_view # 부트스트랩 형태로 보이기
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleSerializer


@api_view(['GET', 'POST'])
def article_list(request):

    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT' , 'DELETE'])
def article_detail(request, pk):

    try:
        articles = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(articles)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(articles, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        articles.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)