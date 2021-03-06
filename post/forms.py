from django.forms import ModelForm, Form
from .models import Post, Comment
from django import forms


class PostForm(ModelForm):
    caption = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
        fields = [
            'photo',
            'caption',
            'location',
            'author',
        ]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]
