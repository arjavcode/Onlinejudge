from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# Create your views here.

from .models import Problem
from accounts import views as api2 

from django.contrib.auth.decorators import login_required

# def registerPage(request):
#     context = {}
#     return render(request, 'judge/register.html' , context)

# def loginPage(request):
#     context = {}
#     return render(request, 'judge/login.html' , context)

# @login_required(login_url='login')   #Showing ERROr
@login_required(login_url='accounts/login/')
def problems(request):
    problem_list = Problem.objects.all()
    context = ({'problem_list': problem_list} )
    return render(request, 'judge/index.html', context)


# @login_required(login_url='login')   #Showing ERROr
@login_required(login_url='accounts/login/')    
def problemDetail(request , problem_id):
    problem = get_object_or_404(Problem, pk=problem_id )
    return render(request , 'judge/detail.html' , {'problem': problem})


