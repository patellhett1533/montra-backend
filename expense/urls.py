from django.urls import path
from .views import AddExpenseView, GetExpenseView, getAllExpenseView

urlpatterns = [
    path('add-expense', AddExpenseView.as_view(), name='add-expense'),
    path('<int:pk>', GetExpenseView.as_view(), name='get-expense'),
    path('', getAllExpenseView.as_view(), name='get-all-expense'),
]