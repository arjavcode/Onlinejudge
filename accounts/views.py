from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
# from judge import views as api1
# Create your views here.

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            
            return redirect('/accounts/login')     #Working fine
            # return redirect('loginuser')        #Showing error


    context = {'form' : form}
    return render(request, 'accounts/register.html' , context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/judge/')                               #Working fine
            # return redirect('problems')                           #Showing error

        else:
            messages.info(request, 'Username or Password is incorrect')
    
    context = {}
    
    return render(request, 'accounts/login.html' , context)

def logoutUser(request):
    logout(request)
    return redirect('/accounts/login')                        #Working fine
    # return redirect('loginuser')                                         #Showing error
