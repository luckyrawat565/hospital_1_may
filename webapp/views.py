from django.shortcuts import render
from .form import user_signup
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = user_signup(request.POST)
        if form.is_valid():
            name = form.cleaned_data['user_name']
            f_name = form.cleaned_data['first_name']
            l_name = form.cleaned_data['last_name']
            p = form.cleaned_data['password1']
            sv = User(username = name, first_name = f_name, last_name = l_name, password = p)
            sv.save()
            return HttpResponse('sucessfully registered')

            
    else:
        form = user_signup()
    return render(request, 'webapp/signup.html',{'form':form})

def logins(request):
    if request.method == "POST":
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = authenticate(username = uname, password = pwd)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('profile/')
    
    else:
        form = AuthenticationForm()
    return render(request, 'webapp/login.html',{'form':form})

def logouts(request):
    logout(request)
    return HttpResponseRedirect('login/')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'webapp/profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('login/')

def change_pass(request):
    return HttpResponse('change password page')



