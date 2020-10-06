from django.shortcuts import render, HttpResponseRedirect, reverse
from instauser import forms, models
from post import models
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):

    def get(self, request):
        posts = models.Post.objects.filter(insta_user=request.user)
        following_posts = models.Post.objects.filter(insta_user__in=request.user.following.all())
        user_following_posts = posts | following_posts
        user_following_posts = user_following_posts.order_by('-time_date')

        return render(request, 'index.html', {'Welcome': 'Welcome to our Instagram Clone', 'posts': user_following_posts, 'count': count})

class ProfileView(TemplateView):

    def get(self, request, user_id):
        profile = models.InstaUser.objects.get(id=user_id)
        posts = models.Post.objects.filter(insta_user=profile)
        user_following = profile.following.all()
        following_list = list(user_following)
        return render(request, 'profile.html', {'profile': profile, 'posts': posts, 'user_following': following_list})


class CreateUserView(TemplateView):

    def get(self, request):
        form = forms.SignupForm()
        return render(request, 'generic_form.html', {'form': form})

    def post(self, request):
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = models.InstaUser.objects.create_user(
                username=data.get('username'),
                password=data.get('password')
            )
            if new_user:
                login(request, new_user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return render(request, 'generic_form.html', {'form': form})


class FollowingView(LoginRequiredMixin, TemplateView):

    def get(self, request, following_id):
        current_user = request.user
        follow = models.InstaUser.objects.filter(id=following_id).first()
        current_user.following.add(follow)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class UnfollowView(LoginRequiredMixin, TemplateView):

    def get(self, request, unfollow_id):
        current_user = request.user
        follow = models.InstaUser.objects.filter(id=unfollow_id).first()
        current_user.following.remove(follow)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))