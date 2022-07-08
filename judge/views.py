from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# Create your views here.

from .models import Problem

def problems(request):
    problem_list = Problem.objects.all()
    context = {'problem_list': problem_list}
    return render(request, 'judge/index.html', context)
    
def problemDetail(request , problem_id):
    problem = get_object_or_404(Problem, pk=problem_id )
    return render(request , 'judge/detail.html' , {'problem': problem})


