from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ExpenseSerializer

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.pk
        serializer = ExpenseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        expenses = Expense.objects.filter(user=request.user)
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)


class ExpenseDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Expense.objects.get(pk=pk, user=self.request.user)
        except Expense.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        expense = self.get_object(pk)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)

    def put(self, request, pk):
        expense = self.get_object(pk)
        data = request.data.copy()
        data['user'] = request.user.pk
        serializer = ExpenseSerializer(expense, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        expense = self.get_object(pk)
        expense.delete()
        return Response({"message": "Expense deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
