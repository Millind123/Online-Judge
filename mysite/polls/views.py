from django.http import HttpResponse
from django.shortcuts import render
from .models import Problems

def problem_statement(request,number):    
    problemset = Problems.objects.all()
    for p in problemset:
        if p.problem_number == number:
            problem=p
    # problem=problemset[0]
    context = {
        'problem':problem
    }
    return render(request, 'polls/problemStatement.html',context)

def index(request):
    problemset=Problems.objects.all();
    context = {
        'problemset':problemset
    }
    return render(request,'polls/index.html',context)