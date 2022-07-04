import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect


from datetime import datetime
from .form import NameForm
from django import forms
from django.shortcuts import render
from .models import Problems,Inputs, Submission


#========================================================================

def problem_statement(request,number):    
    problemset = Problems.objects.all()
    inputset = Inputs.objects.all()
    for p in problemset:
        if p.problem_number == number:
            problem=p
    for i in inputset:
        if i.problem_id==number:
            inputt=i
   

    if request.method == 'POST':
        form = NameForm(request.POST)
        
        if form.is_valid():            
            
            code = form.cleaned_data['code']
            problemID = form.cleaned_data['problemID']
            p = Submission(submission_code=code, submission_verdict = "AC", submission_problemID=problemID)
            p.save()
            print (p)
            submissionSet=Submission.objects.all().order_by('-submission_date')
            # return render (request,'polls/submissionset.html',{'submissionSet':submissionSet})
            return submission_set(request)

    else:
        form = NameForm()       
        print ("not got it")


    context = {
        'problem':problem,
        'inputt':inputt,
        'form': form,
    }


    return render(request, 'polls/problemStatement.html',context)

# =======================================================================
def index(request):
    problemset=Problems.objects.all();
    context = {
        'problemset':problemset
    }
    return render(request,'polls/index.html',context)

# =========================================================

# def get_code(request):
#     if request.method == 'POST':
#         form = NameForm(request.POST)
        
#         if form.is_valid():            
            
#             code = form.cleaned_data['code']
#             problemID = form.cleaned_data['problemID']
#             p = Submission(submission_code=code, submission_verdict = "AC", submission_problemID=problemID)
#             p.save()
#             print (p)

#     else:
#         form = NameForm()       
#         print ("not got it")


#     context = {
#         'form': form
#     }
#     return render(request, 'polls/submissionset.html',context )
# //=====================================================================

def submission_set(request):
    submissionSet=Submission.objects.all().order_by('-submission_date')
    return render (request,'polls/submissionset.html',{'submissionSet':submissionSet})

