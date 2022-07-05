import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect


from datetime import datetime
from .form import NameForm
from django import forms
from django.shortcuts import render
from .models import Problems,Inputs, Submission
import subprocess
import os 


#========================================================================
def getVedict(code , inputts):
    verdict = "AC"
    print (inputts)
    for inputt in inputts:
        inputs= inputt.input_text
        outputs= inputt.input_output
    
        file = str (code) 
        # print (code)
        
        # output = subprocess.run(['output.exe'], capture_output=True, input = input, timeout=10)
        subprocess.run(["g++",file, "-o", "output.exe"])
        output = subprocess.run(['output.exe'], capture_output=True,input =inputs.encode() ,  timeout=10)
        output = output.stdout.decode("utf-8")
        # os.system('g++ algo2.cpp -o a')
        # os.system('./a < input.txt > out.txt')
        # process = subprocess.run(f'g++ {file} -o out; ./out', shell=True, capture_output=True, text=True)
        
        # output = process.stdout.decode() + ' BTW this was runned by Python'
        # print(inputs)
        # print(output)
        # print(outputs)
        if output!=outputs:
            return "WA"
    return "AC"


#========================================================================

def problem_statement(request,number):    
    problemset = Problems.objects.all()
    inputset = Inputs.objects.all()
    inputt=[]
    for p in problemset:
        if p.problem_number == number:
            problem=p
    for i in inputset:
        if i.problem_id==number:
            inputt.append(i)
   

    if request.method == 'POST':
        form = NameForm(request.POST,request.FILES)
        
        if form.is_valid():            
            print ("got it ")
            code = form.cleaned_data['code']
            problemID = number 
            # print(code)
            # problemID = form.cleaned_data['problemID']

            p = Submission(submission_code=code, submission_verdict = getVedict(code,inputt), submission_problemID=problemID)
            p.save()
            submissionSet=Submission.objects.all().order_by('-submission_date')
            # return render (request,'polls/submissionset.html',{'submissionSet':submissionSet})
            return submission_set(request)

    else:
        form = NameForm()       
        print ("not got it")


    context = {
        'problem':problem,
        'inputt':inputt[0],
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

