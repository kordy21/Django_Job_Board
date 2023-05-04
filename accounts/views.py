from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import SignupForm ,ProfileForm , UserForm 
from django.contrib.auth import authenticate , login
from.models import Profile
# Create your views here.

def signup(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # login same username signup
            username=form.cleaned_data=['username']
            password=form.cleaned_data=['password2']
            user = authenticate(username=username, password=password)
            # print("done")
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form})

def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request , 'accounts/profile.html' , {'profile' : profile})

def profile_edit (request):
    profile= Profile.objects.get(user=request.user)
    
    if request.method=='POST':
        user_form = UserForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES,instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            myprofile=profile_form.save(commit=False)
            myprofile.user=request.user
            myprofile.save()  
            return redirect(reverse ('accounts:profile'))
    else:
        user_form=UserForm(instance=request.user)
        profile_form=ProfileForm(instance=profile)
    
    return render(request,'accounts/profile_edit.html',{'user_form':UserForm,'profile_form':ProfileForm})