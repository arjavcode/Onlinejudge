from datetime import timezone
from multiprocessing import context
import os,filecmp
import subprocess
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# Create your views here.

from .models import Problem, Solution, Testcases

from django.contrib.auth.decorators import login_required

# def registerPage(request):
#     context = {}
#     return render(request, 'judge/register.html' , context)

# def loginPage(request):
#     context = {}
#     return render(request, 'judge/login.html' , context)

# @login_required(login_url='login')   #Showing ERROr
@login_required(login_url='/accounts/login')
def problems(request):
    problem_list = Problem.objects.all()
    context = ({'problem_list': problem_list} )
    return render(request, 'judge/index.html', context)


# @login_required(login_url='login')   #Showing ERROr
@login_required(login_url='/accounts/login')    
def problemDetail(request , problem_id):
    problem = get_object_or_404(Problem, pk=problem_id )
    return render(request , 'judge/detail.html' , {'problem': problem})


# @login_required(login_url='login')   #Showing ERROr
@login_required(login_url='/accounts/login')
def submitProblem(request, problem_id):
    if('solution' in request.FILES):
        f = request.FILES['solution']
        with open(r'C:\Users\windows 10\django_tutorial\Onlinejudge\multiply.cpp' , 'wb+') as dest:
            for chunk in f.chunks():
                dest.write(chunk) 
    
    elif('solution' in request.POST):
        code = request.POST['solution']
        f = open(r'C:\Users\windows 10\django_tutorial\Onlinejudge\multiply.cpp' , 'w+')
        f.write(code)
        f.close()

    testcase = Testcases.objects.get(problem = problem_id)

    inputFile = open( r"C:\Users\windows 10\django_tutorial\Onlinejudge\input.txt" , "w")
    n1 = inputFile.write(testcase.input + '\n')
    inputFile.close()

    outputFile = open( r"C:\Users\windows 10\django_tutorial\Onlinejudge\correctOutput.txt" , "w")
    n2 = outputFile.write(testcase.output + '\n')
    outputFile.close()

    compile = r'g++ "C:\Users\windows 10\django_tutorial\Onlinejudge\multiply.cpp" -o "C:\Users\windows 10\django_tutorial\Onlinejudge\solution.exe"'
    # run = r"'C:\Users\windows 10\django_tutorial\Onlinejudge\solution.exe' <"+"\"" +testcase.input + "\""+ r">'C:\Users\windows 10\django_tutorial\Onlinejudge\output.txt'"
    # run = r'"C:\Users\windows 10\django_tutorial\Onlinejudge\solution.exe" <'  +"\"" +testcase.input + "\""+ r'>"C:\Users\windows 10\django_tutorial\Onlinejudge\output.txt"'
    run = r'"C:\Users\windows 10\django_tutorial\Onlinejudge\solution.exe" < '  + r"C:\Users\windows 10\django_tutorial\Onlinejudge\input.txt" + r'>"C:\Users\windows 10\django_tutorial\Onlinejudge\output.txt"'
    
    s = subprocess.check_call(compile,shell=True)
    s = subprocess.check_call(run,shell=True)

    # out1 = r"C:\Users\windows 10\django_tutorial\Onlinejudge\output.txt"
    # out2 = testcase.output

    if(filecmp.cmp(r"C:\Users\windows 10\django_tutorial\Onlinejudge\output.txt", r"C:\Users\windows 10\django_tutorial\Onlinejudge\correctOutput.txt"  , shallow=True)):
        verdict = 'Accepted'
    else:
        verdict = 'Wrong Answer'

    solution = Solution()
    solution.problem = Problem.objects.get(problem_id)
    solution.verdict = verdict
    solution.submitted_at = timezone.now()
    solution.submitted_code =  r"g++ C:\Users\windows 10\django_tutorial\Onlinejudge\solution.cpp"
    solution.save() 

    return HttpResponseRedirect(reverse('judge:leaderboard'))

def leaderboard(request):
    solutions = Solution.objects.all()
    return render(request, 'judge/leaderboard.html' , {'solutions':solutions})























