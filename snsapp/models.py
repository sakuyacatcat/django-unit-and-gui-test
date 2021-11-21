from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.ManyToManyField(
        User, related_name='related_post', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def extract_post_liked_by_specified_user(user_object):
        return Post.objects.filter(like=user_object.id)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Connection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(
        User, related_name='following', blank=True)

    def __str__(self):
        return self.user.username
