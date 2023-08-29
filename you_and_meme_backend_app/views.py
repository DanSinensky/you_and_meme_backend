from rest_framework import viewsets

from .serializers import ProfileSerializer, PostSerializer, CommentSerializer, UserSerializer, TokenSerializer
from .models import Profile, Post, Comment


from rest_framework import generics, status, permissions
# from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# from rest_framework_simplejwt import views as jwt_views


from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(generics.ListCreateAPIView):
    """
    POST user/login/
    """

    # This permission class will overide the global permission class setting
    # Permission checks are always run at the very start of the view, before any other code is allowed to proceed.
    # The permission class here is set to AllowAny, which overwrites the global class to allow anyone to have access to login.
    # permission_classes = [IsAdminUser]
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            refresh = RefreshToken.for_user(user)
            serializer = TokenSerializer(data={
                # using DRF JWT utility functions to generate a token
                "token": str(refresh.access_token)
            })
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegisterUsersView(generics.ListCreateAPIView):
    """
    POST user/signup/
    """
    # permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username or not password or not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(status=status.HTTP_201_CREATED)


# class CustomTokenObtainPairView(jwt_views.TokenObtainPairView):
#     permission_classes = [IsAdminUser]


# class CustomTokenRefreshView(jwt_views.TokenRefreshView):
#     permission_classes = [IsAdminUser]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsAdminUser]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAdminUser]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [IsAdminUser]
