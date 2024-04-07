from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status,generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserRegistrationSerializers,UserProfileSerializer,UserReferralSerializer,LoginSerializers
from rest_framework_simplejwt.tokens import RefreshToken


# generate token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    """
    User registration view.

    POST Request:
    - Receives user registration data.
    - Validates and saves the user.
    - Returns success message, user ID, and token on successful registration.
    - Returns error messages on invalid data.

    Methods:
    - post(request, format=None): Handles user registration requests.
    """
    
    def post(self, request, format=None):
        """
        Handles user registration requests.

        Returns:
        - Success message, user ID, and token on successful registration.
        - Error messages on invalid data.
        """
        serializer = UserRegistrationSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'msg': 'Registration Success', 'User_ID': user.pk, 'token': token}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    """
    User login view.

    POST Request:
    - Receives user login data.
    - Authenticates user.
    - Returns token and success message on login.

    Methods:
    - post(request, format=None): Handles user login requests.
    """
    
    def post(self, request, format=None):
        """
        Handles user login requests.

        Returns:
        - Token and success message on login.
        """
        serializer = LoginSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=email,password=password)
            if user:
                token = get_tokens_for_user(user)
                return Response({'token': token, 'msg': 'Login valid for 10 minutes'}, status=status.HTTP_200_OK)
        return Response({'msg': 'Login Failed'}, status=status.HTTP_400_BAD_REQUEST)
    

class UserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Retrieve user profile information.
        """
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class ReferralView(generics.RetrieveAPIView):
    """
    Retrieve the user's referral information.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserReferralSerializer

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
