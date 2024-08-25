from django.urls import path
from .views import TransferView, TransferDetailView

urlpatterns = [
    path('', TransferView.as_view()),
    path('<int:pk>/', TransferDetailView.as_view()),
]
