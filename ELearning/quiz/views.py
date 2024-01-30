from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Quiz, Category
from django.db.models import Q
from .models import QuizSubmission
from account.models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
import razorpay

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

@login_required(login_url='login')
def quiz_view(request, quiz_id):
    quiz = Quiz.objects.filter(id=quiz_id).first()

    total_questions = quiz.question_set.all().count()

    if request.method == "POST":
        score = int(request.POST.get('score', 0))

        # Check if the user has already submiited the quiz
        if QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists():
            messages.success(request, f"This time you got {score} out of {total_questions}")
            return redirect('quiz_view', quiz_id)
        
        # save the new quiz submission
        submission = QuizSubmission(user=request.user, quiz=quiz, score=score)
        submission.save()

        # show the result in message
        messages.success(request,f"Quiz Submitted Successfully. You got {score} out of {total_questions}")
        return redirect('quiz_view', quiz_id)

    if quiz != None:
        context={
            'quiz': quiz
        }
    else:
        return redirect('all_quiz')
    return render(request, 'quiz.html', context)


def notes_view(request):

    prem_users_object = Profile.objects.filter(is_premium=True)
    

    if request.user.is_authenticated and request.user.profile.is_premium:
        return render(request, 'notes.html')
    else:
        client = razorpay.Client(auth=("rzp_test_J1OkBRgRlsXW8y", "qendIyZDFqTznlmVOp1XoGRR"))
        amount= 500
        payment = client.order.create({'amount': amount, 'currency': 'INR'})
        
        #user_object = User.objects.get(username=request.user)
        user_profile = Profile.objects.filter(user=request.user).update(is_premium=True)
        user_name = Profile.objects.filter(user=request.user)
        #user_profile.update(is_premium=True)
        context={
            'amount': amount,
            'user_name': user_name,
            
        }

        return render(request, 'payment.html')
    