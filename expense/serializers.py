from rest_framework import serializers
from expense.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'user', 'description', 'amount', 'date']

    # def create(self, validated_data):
    #     return Expense.objects.create(**validated_data)
