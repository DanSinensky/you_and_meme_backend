from .serializers import ProfileSerializer, PostSerializer, CommentSerializer, UserSerializer, TokenSerializer, MemeSerializer
from .models import Profile, Post, Comment, Meme

from rest_framework import viewsets, status
from rest_framework import generics, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.hashers import make_password

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
        avatar = request.data.get("avatar", "")
        if not username or not password or not email:
            return Response(
                data={
                    "message": "Username, password and email is required to register a user."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email, avatar=avatar
        )
        return Response(status=status.HTTP_201_CREATED)


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)

    @action(detail=True, methods=['PUT'])
    def update_username(self, request, pk=None):
        profile = self.get_object()
        new_username = request.data.get("username", None)

        if new_username is not None:
            profile.user.username = new_username
            profile.user.save()
            return Response({"message": "Username updated successfully."})
        else:
            return Response({"message": "Username field is required to update username."}, status=400)

    @action(detail=True, methods=['PUT'])
    def update_password(self, request, pk=None):
        profile = self.get_object()
        new_password = request.data.get("password", None)

        if new_password is not None:
            user = profile.user
            user.password = make_password(new_password)
            user.save()

            update_session_auth_hash(request, user)

            return Response({"message": "Password updated successfully."})
        else:
            return Response({"message": "Password field is required to change the password."}, status=400)

    @action(detail=True, methods=['PUT'])
    def add_to_liked_posts(self, request, pk=None):
        profile = self.get_object()
        new_numbers = request.data.get("likedPosts", [])

        if new_numbers:
            profile.likedPosts.extend(new_numbers)
            profile.save()

            return Response({"message": "Numbers added to likedPosts successfully."})
        else:
            return Response({"message": "No numbers provided to add to likedPosts."}, status=400)


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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        likes = request.data.get("likes", None)

        if likes is not None:
            instance.likes = likes
            instance.save()

            return Response(
                data={
                    "message": "Likes updated successfully."
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data={
                    "message": "Likes field is required to update likes."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MemeViewSet(viewsets.ModelViewSet):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
