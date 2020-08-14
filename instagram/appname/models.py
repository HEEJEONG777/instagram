from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Post(models.Model):
    def __str__(self):
        return self.location
        
    location = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="writer", default="")

    hashtag_field = models.CharField(max_length=200, blank=True)
    hashtags = models.ManyToManyField('Hashtag', blank=True)

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likes")


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

    nickname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    face_img = models.ImageField(upload_to='images/', blank=True)

class Comment(models.Model):
    def __str__(self):
        return self.text
            
    c_writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="c_writer", default="")
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=50)

class Hashtag(models.Model):
    def __str__(self):
        return self
    name = models.CharField(max_length=50)