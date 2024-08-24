from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user_data = UserSerializers(user).data
            return Response({"user": user_data}, status=201)
        return Response(serializer.errors, status=400)


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.get(email=email)
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)
            return Response({'data': UserSerializers(user).data, 'refresh_token': refresh_token, 'access_token': access_token}, status=200)
        return Response({'error': "Invalid credentials"}, status=400)


class LogoutView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'User logged out successfully'})
