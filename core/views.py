from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from .models import Feedback
from .forms import FeedbackCreateForm, SignInForm


def price_view(request):
    return render(request, "core/price.html")


def feedback_view(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        feedback = Feedback()
        feedback.first_name = data['first_name']
        feedback.rating = int(data['rating'])
        feedback.text = data['text']
        feedback.contact = data['contact']
        feedback.save()
        return HttpResponse("Ваш отзыв принят!")
    return render(request, 'core/feedback.html')


def feedback_form_view(request):
    context = {}

    if request.method == "POST":
        feedback_create_form = FeedbackCreateForm(request.POST)
        feedback_create_form.save()


    feedback_create_form = FeedbackCreateForm()
    context["feedback_create_form"] = feedback_create_form
    return render(request, 'core/feedback_form.html', context)


def sign_in(request):
    if request.method == "POST":
        auth_form = SignInForm(request.POST)
        if auth_form.is_valid():
            user = authenticate(
                request,
                username=auth_form.validated_data['username'],
                password=auth_form.validated_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('homepage')

    context = {'auth_form': SignInForm()}
    return render(request, 'core/sign_in.html',context)