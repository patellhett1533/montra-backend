from rest_framework.viewsets import ModelViewSet
from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseApi(ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
