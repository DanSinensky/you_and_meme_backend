from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.username}'


# class Like(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='likes')

#     def __str__(self):
#         return f'{len(self.user)} likes'


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    meme = models.TextField()
    likes = models.IntegerField(default=0)
    # likes = models.ForeignKey(
    #     Like, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.user}\'s Post'


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()

    def __str__(self):
        return f''
