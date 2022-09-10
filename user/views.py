from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import RegisterUserForm

# Create your views here.
def user_register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect("/")
        else:
            print(form.cleaned_data)
            print(form.errors)
            return redirect("/user/register")
    else:
        form = RegisterUserForm()
    return render(request, "user/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("Success login!")
            login(request, user)
            return redirect('/user/profile')
        else:
            print("Failure login!")
            #Check admin dashboard for count of invalid attemps, if count to 3 send an email for unauthorized access.
            messages.success(request, ("Authentication Error! Please try again!"))
            return redirect('/user/login')
    else:
        return render(request, "user/login.html", {})

def user_profile(request):
    return render(request, "user/profile.html")