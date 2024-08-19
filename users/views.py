from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializers
from .models import User
from rest_framework_jwt.settings import api_settings

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': "User Created Successfully"}, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.get(email=email)
        if user and user.check_password(password):
            payload = api_settings.JWT_PAYLOAD_HANDLER(user)
            token = api_settings.JWT_ENCODE_HANDLER(payload)
            return Response({'token': token})
        return Response ({'error': "Invalid credentials"}, status=400)
    
class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'User logged out successfully'})