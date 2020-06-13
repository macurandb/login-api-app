from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

from .serializers import UserSerializer, UserSigninSerializer

from .authentication import token_expire_handler, expires_in
@api_view(["GET"])
def user_info(request):
    return Response({
        'user': request.user.email,
        'expires_in': expires_in(request.auth)
    }, status=HTTP_200_OK)


class SignInAPI(APIView):
    """
        Sign in method with "email" and "password"
        ---
        parameters:
           - name: email
             required: true
             type: string
           - name: password
             required: true
             type: string
             return ('token', user}
    """
    serializer_class = UserSigninSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        signin_serializer = UserSigninSerializer(data=request.data)
        if not signin_serializer.is_valid():
            return Response(signin_serializer.errors, status=HTTP_400_BAD_REQUEST)

        user = authenticate(
            username=signin_serializer.data['email'],
            password=signin_serializer.data['password']
        )
        if not user:
            return Response({'detail': 'Invalid Credentials or activate account'}, status=HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user)

        is_expired, token = token_expire_handler(token)
        user_serialized = UserSigninSerializer(user)

        return Response({
            'user': user_serialized.data,
            'expires_in': expires_in(token),
            'token': token.key
        }, status=HTTP_200_OK)

class RegisterUserAPI(generics.CreateAPIView):

    serializer_class = UserSerializer
    permission_classes = [AllowAny]