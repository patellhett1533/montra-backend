from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tranfer
from .serializers import TranferSerializer


class TranferView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transfers = Tranfer.objects.filter(user=request.user)
        serializer = TranferSerializer(transfers, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.pk
        serializer = TranferSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TranferDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Tranfer.objects.get(pk=pk, user=self.request.user)
        except Tranfer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        transfer = self.get_object(pk)
        serializer = TranferSerializer(transfer)
        return Response(serializer.data)

    def put(self, request, pk):
        transfer = self.get_object(pk)
        data = request.data.copy()
        data['user'] = request.user.pk
        serializer = TranferSerializer(transfer, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        transfer = self.get_object(pk)
        transfer.delete()
        return Response({"message": "Transfer deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
