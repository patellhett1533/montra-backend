from django.urls import path
from .views import ExpenseView, ExpenseDetailView

urlpatterns = [
    path('api', ExpenseView.as_view()),
    path('<int:pk>/', ExpenseDetailView.as_view()),
]