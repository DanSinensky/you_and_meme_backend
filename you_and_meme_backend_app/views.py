from rest_framework import viewsets

from .serializers import ProfileSerializer, PostSerializer, CommentSerializer, UserSerializer, TokenSerializer, MemeSerializer
from .models import Profile, Post, Comment, Meme


from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken


class CustomToken(RefreshToken):

    @classmethod
    def for_user(cls, user):
        token = super(CustomToken, cls).for_user(user)

        token.payload['username'] = user.username
        return token


class LoginView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = CustomToken.for_user(user)
            serializer = TokenSerializer(data={
                "token": str(refresh.access_token)
            })
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegisterUsersView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username or not password or not email:
            return Response(
                data={
                    "message": "Username, password and email is required to register a user."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(status=status.HTTP_201_CREATED)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        meme = request.data.get("meme", "")
        if not meme:
            return Response(
                data={
                    "message": "Meme url is required to create a post."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_post = Post.objects.create_post(
            meme=meme
        )
        return Response(status=status.HTTP_201_CREATED)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        body = request.data.get("body", "")
        if not body:
            return Response(
                data={
                    "message": "Text body is required to create a comment."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_comment = Comment.objects.create_comment(
            body=body
        )
        return Response(status=status.HTTP_201_CREATED)


class MemeViewSet(viewsets.ModelViewSet):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
