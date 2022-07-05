import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from datetime import datetime
from .form import NameForm
from django import forms
from django.shortcuts import render
from .models import Problems,Inputs, Submission
import subprocess



#========================================================================

def getVedict(code , inputts):
    
    print (inputts)
    for inputt in inputts:
        inputs= inputt.input_text
        outputs= inputt.input_output
    
        file = str (code) 
        # print (code)
        
        # output = subprocess.run(['output.exe'], capture_output=True, input = input, timeout=10)
        subprocess.run(["g++",file, "-o", "output.exe"])
        # try:
        
        output = subprocess.run(['output.exe'], capture_output=True,input =inputs.encode() ,  timeout = 5)
        error = output.stderr.decode ("utf-8")
        # if error!=0:
        #     return "RE"
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

@login_required(login_url="/login")
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
            subID = len(Submission.objects.all())+1
            p = Submission(username=request.user.username,submission_ID=subID,submission_code=code,submission_verdict=getVedict(code,inputt), submission_problemID=problemID)
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

@login_required(login_url="/login")
def index(request):
    username = request.user.username
    print(username)
    problemset=Problems.objects.all();
    context = {
        'problemset':problemset
    }
    return render(request,'polls/index.html',context)

# =========================================================


@login_required(login_url="/login")
def submission_set(request):
    submissionSet=Submission.objects.all().order_by('-submission_date')
    return render (request,'polls/submissionset.html',{'submissionSet':submissionSet})



# ==============================================================================


@login_required(login_url="/login")
def veiw_submission(request , subID):
    submission_set=Submission.objects.all()
    for sub in submission_set:
        if sub.submission_ID==subID:
            submission=sub
    
    f = submission.submission_code
    with open(str (f), 'r') as file:
        data = file.read().replace('/n', '<br>')

    return render (request,'polls/veiwSubmission.html',{'submission':submission,'data':data})