from rest_framework import serializers
from .models import Profile, Post, Comment, Meme
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [f.name for f in Post._meta.fields] + ['comments']


class ProfileSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    # likedPosts = LikeSerializer(many=True, read_only=True)
    user_string = serializers.ReadOnlyField(
        source='user.username')

    class Meta:
        model = Profile
        fields = [f.name for f in Profile._meta.fields] + \
            ['posts', 'likedPosts', 'user_string']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = '__all__'
