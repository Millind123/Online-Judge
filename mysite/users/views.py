from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print ("helo")

        if form.is_valid():   
            form.save()         
            username=form.cleaned_data['username']
            # messages.success(request,f'account created for {username}!!')
            print("got username")
            print (username)
            return redirect('/login')
    else: 
        form = UserCreationForm()
        print ("not got it ")
   
    return render (request,'users/register.html',{'form':form})
