from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import IncomeSerializer
from .models import Income

# Create your views here.


class IncomeView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = IncomeSerializer

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.pk
        serializer = IncomeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        expenses = Income.objects.filter(user=request.user)
        serializer = IncomeSerializer(expenses, many=True)
        return Response(serializer.data)


class IncomeDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Income.objects.get(pk=pk, user=self.request.user)
        except Income.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        expense = self.get_object(pk)
        serializer = IncomeSerializer(expense)
        return Response(serializer.data)

    def put(self, request, pk):
        expense = self.get_object(pk)
        data = request.data.copy()
        data['user'] = request.user.pk
        serializer = IncomeSerializer(expense, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        expense = self.get_object(pk)
        expense.delete()
        return Response({"message": "Income deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
