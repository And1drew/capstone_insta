import re
from django.shortcuts import render, HttpResponseRedirect, reverse
from post import forms, models
from instauser.models import InstaUser
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class PostView(TemplateView):

    def get(self, request, tweet_id):
        post = models.Post.objects.filter(id=tweet_id).first()
        return render(request, 'post.html', {'Post': post})


class CreatePostView(LoginRequiredMixin, TemplateView):

    def get(self, request):
        form = forms.PostForm()
        return render(request, 'generic_form.html', {'form': form})

    def post(self, request):
        form = forms.TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            at_user = re.findall(r'@([\w]+)', data.get('post'))
            new_post = models.Post.objects.create(
                post = data.get('post'),
                insta_user= request.user
            )

