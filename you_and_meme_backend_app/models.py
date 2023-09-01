from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# class Like(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='likes')

#     def __str__(self):
#         return f'{len(self.user)} likes'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user}'

    def user_string(self):
        return f'{self.user}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Post(models.Model):
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='posts')
    meme = models.TextField()
    likes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # likes = models.ForeignKey(
    #     Like, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.user}\'s post\nid: {self.id}\nlikes: {self.likes}\ncreated: {self.created}'


class Comment(models.Model):
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}\'s comment on Post {self.post.id}\nid: {self.id}\ncreated: {self.created}'


class Meme(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    url = models.TextField()
    width = models.IntegerField()
    height = models.IntegerField()
    box_count = models.IntegerField()

    def __str__(self):
        return f'{self.name}'
