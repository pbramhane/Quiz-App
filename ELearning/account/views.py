from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        if form.is_valid():
            form.save()
            user_model = User.objects.get(username=username)
            Profile.objects.create(user=user_model, email=email)
            return redirect('login')
        

    
    context = {'registerform': form}

    return render(request, 'register.html', context)


def userlogin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                #return render(request, 'index.html')
                return redirect('home')
    
    context = {
        'loginform': form,
        }

    return render(request, 'login.html', context) 

@login_required(login_url='login')
def userLogout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile(request, username):
    user_object = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user_object)

    context = {
        'user_profile': user_profile,
    }
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def editProfile(request):

    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        profile_img = request.FILES.get('profile_img')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        location = request.POST.get('location')
        gender = request.POST.get('gender')
        bio = request.POST.get('bio')
        
        if profile_img:
            user_profile.profile_img=profile_img
        if firstname:
            user_object.first_name = firstname
        if lastname:
            user_object.last_name = lastname
        if email:
            user_profile.email = email
            user_object.email = email
        if username:
            user_object.username = username
        if location:
            user_profile.location = location
        if gender:
            user_profile.gender = gender
        if bio:
            user_profile.bio = bio
        
        user_profile.save()
        user_object.save()
        return redirect('profile', user_object.username)

    context = {
        'user_profile': user_profile,
    }
    return render(request, 'profile-edit.html', context)


@login_required(login_url='login')
def deleteProfile(request):

    user_object = User.objects.get(username=request.user)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == "POST":
        user_profile.delete()
        user_object.delete()
        return redirect('logout')

    return render(request, 'confirm.html')