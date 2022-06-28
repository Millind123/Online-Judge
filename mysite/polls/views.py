from django.http import HttpResponse
from django.shortcuts import render
from .models import Problems,Inputs

def problem_statement(request,number):    
    problemset = Problems.objects.all()
    inputset = Inputs.objects.all()
    for p in problemset:
        if p.problem_number == number:
            problem=p
    for i in inputset:
        if i.problem_id==number:
            inputt=i
    context = {
        'problem':problem,
        'inputt':inputt
    }
    return render(request, 'polls/problemStatement.html',context)

def index(request):
    problemset=Problems.objects.all();
    context = {
        'problemset':problemset
    }
    return render(request,'polls/index.html',context)