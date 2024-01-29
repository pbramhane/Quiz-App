from django.shortcuts import render
from quiz.models import UserRank
from django.contrib.auth.decorators import login_required
from account.models import Profile
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.
def home(request):
    leaderboard_users = UserRank.objects.order_by('rank')[:3]

    context = {
        'leaderboard_users': leaderboard_users,
    }

    return render(request, 'index.html', context)


@login_required(login_url='login')
def leaderboard_view(request):

    leaderboard_users = UserRank.objects.order_by('rank')

    context = {
        'leaderboard_users': leaderboard_users,
    }

    return render(request, 'leaderboard.html', context)


def search_users(request):
    query = request.GET.get('q')

    if query:
        users = User.objects.filter(
            Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query)
        ).order_by('date_joined')

    else:
        users = []

    if request.user.is_authenticated:
        # request user
        user_object = User.objects.get(username=request.user)
        user_profile = Profile.objects.get(user=user_object)
        context = {"user_profile": user_profile, "query": query, "users": users}
    else:
        context = {"query": query, "users": users}
    return render(request, 'search-users.html', context)




