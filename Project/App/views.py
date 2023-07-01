from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def base(request):
    return  render(request,'Base.html')

def register_user(request):
    if request.method=='POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username1 = form.cleaned_data.get('username')
            messages.success(request,f"Hello {username1}, your account has been created")
            return redirect('Success')
        else:
            form = NewUserForm()
    form = NewUserForm()
    return  render(request,'register.html',{'register_form':form})

@login_required()
def profile(request):
    return  render(request,'profile.html')
def profile1(request):
    return  render(request,'profile1.html')
def Success(request):
    return render(request,'Success.html')
# Create your views here.
def About(request):
    return render(request,'About.html')
def About1(request):
    return render(request,'About1.html')

def Contact(request):
    return render(request,'Contact.html')
def Contact1(request):
    return render(request,'Contact1.html')