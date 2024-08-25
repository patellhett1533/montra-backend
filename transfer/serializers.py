from rest_framework import serializers
from transfer.models import Tranfer


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tranfer
        fields = ['id', 'user', 'name', 'amount', 'date']
