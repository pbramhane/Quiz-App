from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html')

def takeQuiz(request):
    return render(request, 'allQuiz.html')

def register(request):
    return render(request, 'register.html')

def profile(request):
    return render(request, 'profile.html')