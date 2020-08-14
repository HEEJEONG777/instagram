from django import forms
from .models import Post, CustomUser, Comment, Hashtag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['location', 'content', 'image', 'hashtag_field']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']

class SignForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'nickname', 'phone_number', 'face_img']

class CommentForm(forms.ModelForm):
    text = forms.CharField(label='')
    class Meta:
        model = Comment
        fields = ['text']