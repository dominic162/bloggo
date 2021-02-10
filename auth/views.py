from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from auth import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from mainapp import models

# Create your views here.
def auth_login(request):
    if(request.user.is_authenticated):
        return HttpResponseRedirect('/bloggo')
    loginform=forms.login()
    context={
        'form':loginform,
    }
    if(request.method=="POST"):
        loginform=forms.login(request.POST)
        if loginform.is_valid():
            username=loginform.cleaned_data['username']
            password=loginform.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return HttpResponseRedirect("/bloggo")
        context={
            'error':True,
            'form':forms.login(request.POST),
        }
    return render(request,'auth/login.html',context)

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/bloggo')

def auth_signup(request):
    if(request.user.is_authenticated):
        return HttpResponseRedirect('/bloggo')
    signupform=forms.signup()
    context={
        'form':signupform,
    }
    if(request.method=="POST"):
        request.POST=request.POST.copy()
        request.POST['slug']=request.POST['username']

        signupform=forms.signup(request.POST,request.FILES)

        if(signupform.is_valid()):
            username=signupform.cleaned_data['username']
            password=signupform.cleaned_data['password']
            try:
                user=User.objects.get(username=username)
                context['error']=True
                context['form']=forms.signup(request.POST)
            except:
                user=User.objects.create_user(username=username,password=password)
                login(request,user)
                signupform.save()
                return HttpResponseRedirect('/bloggo')
    return render(request,'auth/signup.html',context)