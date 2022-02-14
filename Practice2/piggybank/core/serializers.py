from rest_framework import serializers

from .models import Currency, Category, Transaction


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("id", "code", "name")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


# class TransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transaction
#         fields = (
#             "amount",
#             "currency",
#             "date",
#             "description",
#             "category",
#         )
#
# 진행중
# URL : https://www.youtube.com/watch?v=46zLzePAcsU&list=PLLxk3TkuAYnrO32ABtQyw2hLRWt1BUrhj&index=2