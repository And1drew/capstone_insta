from django import forms
from post.models import Post
from django.forms import Textarea


class TweetForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post']
        widgets = {
            'post': Textarea(attrs={'onkeyup':"countChar(this)"})
        }