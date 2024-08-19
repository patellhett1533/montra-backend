from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Expense
from .serializers import ExpenseSerializer

class AddExpenseView(generics.CreateAPIView):
    serializer_class = ExpenseSerializer
    permissions_class = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GetExpenseView(generics.RetrieveAPIView):
    queryset = Expense.objects.all()
    serializers_class = ExpenseSerializer
    permissions_class = [permissions.IsAuthenticated]

class getAllExpenseView(generics.ListAPIView):
    serializers_class = ExpenseSerializer
    permissions_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)