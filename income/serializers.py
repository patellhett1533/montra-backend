from rest_framework import serializers
from .models import Income


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'user', 'description', 'amount']


class AddIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'user', 'description', 'amount']

    def create(self, validated_data):
        return Income.objects.create(**validated_data)
