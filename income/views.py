from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import IncomeSerializer

# Create your views here.


class IncomeView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = IncomeSerializer

    def get_queryset(self):
        return ({'pk': "self.request.user.pk"})
        # return Income.objects.filter(user=self.request.user)

    def get(self, request):
        income = self.get_queryset()
        serializer = IncomeSerializer(income, many=True)
        return Response(serializer.data)
