from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Quiz, Category
from django.db.models import Q

# Create your views here.

@login_required(login_url='login')
def all_quiz_view(request):
    quizzes = Quiz.objects.all().order_by('-created_at')
    categories = Category.objects.all()

    context={
        'quizzes': quizzes,
        'categories': categories,

    }
    return render(request, 'allQuiz.html', context)

@login_required(login_url='login')
def searchView(request, category):

    if request.GET.get('q') != None:
        q = request.GET.get('q')
        query = Q(title__icontains=q) | Q(description__icontains=q)
        quizzes = Quiz.objects.filter(query).order_by('-created_at')
    
    elif category != " ":
        quizzes = Quiz.objects.filter(category__name=category).order_by('-created_at')
    
    else:
        quizzes = Quiz.objects.order_by('-created_at')

    categories = Category.objects.all()

    context={
        'quizzes': quizzes,
        'categories': categories,

    }
    return render(request, 'allQuiz.html', context)