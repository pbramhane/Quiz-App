from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def takeQuiz(request):
    return render(request, 'allQuiz.html')

""" def register(request):
    return render(request, 'register.html') """

def profile(request):
    return render(request, 'profile.html')

def quiz(request):
    return render(request, 'quiz.html')

def userlogin(request):
    return render(request, 'login.html')