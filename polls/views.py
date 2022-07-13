from asyncio import exceptions
import datetime
import py_compile
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from datetime import datetime
from .form import NameForm
from django import forms
from django.shortcuts import render
from .models import Problems,Inputs,Submission
import subprocess,re



#========================================================================
def getVerdictJ (subID ,filename,inputts):
        codefile = f'AllData/codes/{subID}/{filename}'
        codefilename = filename
        complete= subprocess.run(f'docker run -d java tail -f /dev/null',capture_output=True)
        containerId = complete.stdout.decode()[:-1]
        subprocess.run(f'docker cp {codefile} {containerId}:/{codefilename}')
        subprocess.run(f'docker exec {containerId} javac {codefilename} ')

        filenamewithoutjava=(codefilename)[:-5]
        print ("^^^^"+filenamewithoutjava)
        for inputt in inputts:
            inputfile = inputt.inputfile
            outfile = inputt.outputfile
            # print (infile)
            gotoutputfile = 'AllData/gotoutput.txt'
            # inputfile = 'AllData/inputs/i11_qE58CBV.txt'
            # outputfile = open ((gotoutfile),'w')
            # inputfile = open ((infile),'r')
            subprocess.run(f'docker cp {inputfile} {containerId}:/input.txt')
            subprocess.run(f'docker exec -it {containerId} sh -c "java {filenamewithoutjava} <input.txt> output.txt"')
            subprocess.run(f'docker cp {containerId}:/output.txt {gotoutputfile}')

            # subprocess.run( f'java {codefile} < {infile} > {gotoutfile}',shell=True)
                        
            with open(gotoutputfile, 'r') as file:
                data1 = file.read()

            with open(str(outfile), 'r') as file:
                data2 = file.read()
            print("got file " + data1)
            print("got file "+ data2)
            
            data1 = re.sub('[\n ]','',data1)
            data2 = re.sub('[\n ]','',data2)
            if data1!=data2:
                print("wrong ans ")
                subprocess.run(f'docker rm -f {containerId}')

                return "WA"
        subprocess.run(f'docker rm -f {containerId}')
        return "AC"

def getVerdictP (subID ,filename, inputts):
        codefile = f'AllData/codes/{subID}/{filename}'
        
        complete= subprocess.run(f'docker run -d python tail -f /dev/null',capture_output=True)
        containerId = complete.stdout.decode()[:-1]
        subprocess.run(f'docker cp {codefile} {containerId}:/code.py')
        
        for inputt in inputts:
            inputfile = inputt.inputfile
            outfile = inputt.outputfile
            print (inputfile)
            gotoutputfile = 'AllData/gotoutput.txt'
            subprocess.run(f'docker cp {inputfile} {containerId}:/input.txt')
            subprocess.run(f'docker exec -it {containerId} sh -c "python code.py <input.txt> output.txt"')
            subprocess.run(f'docker cp {containerId}:/output.txt {gotoutputfile}')

            # inputfile = 'AllData/inputs/i11_qE58CBV.txt'
            # outputfile = open ((gotoutfile),'w')
            # inputfile = open ((infile),'r')
            # subprocess.run( f'py {codefile} < {infile} > {gotoutfile}',shell=True)
                        
            with open(gotoutputfile, 'r') as file:
                data1 = file.read()

            with open(str(outfile), 'r') as file:
                data2 = file.read()

            data1 = re.sub('[\n ]','',data1)
            data2 = re.sub('[\n ]','',data2)
            
            if data1!=data2:
                print("wrong ans ")
                subprocess.run(f'docker rm -f {containerId}')
                return "WA"

        subprocess.run(f'docker rm -f {containerId}')
        return "AC"


def getVerdictC (subID ,filename,inputts):
    # codefile = str (code)
    # print (codefile)
    codefile = f'AllData/codes/{subID}/{filename}'

    complete= subprocess.run(f'docker run -d gcc tail -f /dev/null',capture_output=True)
    containerId = complete.stdout.decode()[:-1]

    # with open(str(codefile), 'r') as file:
            # data2 = file.read()
    # print("incode = " + data2)
    subprocess.run(f'docker cp {codefile} {containerId}:/code.cpp')

    subprocess.run(f'docker exec {containerId} g++ code.cpp -o r')
        
    # subprocess.run(["g++",codefile, "-o", "out1"],shell = True)
    # print(codefile)
    # print (inputts)
    for inputt in inputts:
        inputs= inputt.input_text
        outputs= inputt.input_output
        inputfile = inputt.inputfile
        outputfile = inputt.outputfile
        gotoutputfile = 'AllData/gotoutput.txt'
        print (codefile)
        # with open(gotoutfile, 'r') as file:
            # data1 = file.read()
            
        subprocess.run(f'docker cp {inputfile} {containerId}:/input.txt')
        subprocess.run(f'docker exec -it {containerId} sh -c "./r <input.txt> output.txt"')
        subprocess.run(f'docker cp {containerId}:/output.txt {gotoutputfile}')

        # print("contents of gotout before sp = " +data1)
        # subprocess.run(f'out1 < {infile} > {gotoutfile}',shell = True,capture_output=True )
        
        with open(gotoutputfile, 'r') as file:
            data1 = file.read()
        print("after sp gotout=" + data1)
        
        with open(str(outputfile), 'r') as file:
            data2 = file.read()
        print("outfile = " + data2)
        
        # output = subprocess.run(['output.exe'], capture_output=True, input = input, timeout=10)
        # subprocess.run(["g++",file, "-o", "output.exe"])
        # try:
        
        # output = subprocess.run(['output.exe'], capture_output=True,input =inputs.encode() ,  timeout = 5)
        # error = output.stderr.decode ("utf-8")
        # if error!=0:
        #     return "RE"
        # output = output.stdout.decode("utf-8")
        # os.system('g++ algo2.cpp -o a')
        # os.system('./a < input.txt > out.txt')
        # process = subprocess.run(f'g++ {file} -o out; ./out', shell=True, capture_output=True, text=True)
        
        # output = process.stdout.decode() + ' BTW this was runned by Python'
        # print(inputs)
        # print(output)
        # print(outputs)
        data1 = re.sub('[\n ]','',data1)
        data2 = re.sub('[\n ]','',data2)
        if data1!=data2:
            subprocess.run(f'docker rm -f {containerId}')
            print("wrong ans ")
            return "WA"
    subprocess.run(f'docker rm -f {containerId}')
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
            language= form.cleaned_data['language']
            print(language)
            if language=="python":
                language="py"
            if language=='c++':
                language="cpp"
            problemID = number 

            subID = len(Submission.objects.all())+1
            ver ="ac"
            print (code)
            filename=str (code)
            print (filename)
            print (language)
            p = Submission(submission_language=language, username=request.user.username,submission_ID=subID,submission_code=code,submission_verdict=ver, submission_problemID=problemID)
            p.save()
            if language=="cpp":
                ver=getVerdictC(subID,filename,inputt)
                p.submission_verdict=ver
                p.save()
            if language=="py":
                ver=getVerdictP(subID,filename,inputt)
                p.submission_verdict=ver
                p.save ()
            if language=='java':
                ver=getVerdictJ(subID,filename,inputt)
                p.submission_verdict=ver
                p.save ()
            

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