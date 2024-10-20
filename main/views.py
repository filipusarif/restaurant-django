from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,authenticate, get_user_model,logout
from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
User = get_user_model()


@login_required(login_url="login/owner")
def show_main(request):
    if request.user.role == 1:
        return render(request,"customer_homepage.html")
    return render(request,"owner_homepage.html")

def login_owner(request):
    form = AuthenticationForm()
    debug = "NO"
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            debug = "YES"
            user = form.get_user()
            if user.role == 1:
                messages.error(request,"Not registered as a owner!")
            else:
                login(request,user)
                return redirect("main:show_main")
    else:
        form = AuthenticationForm()
    context = {'form':form, 'debug':debug}
    return render(request,"auth/owner_login.html",context)

def register_owner(request):
    form = CustomUserCreationForm()
    debug = "no"
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            debug="yes"
            user = form.save(commit=False)
            user.role = 0
            user.save()
            return redirect("main:show_main")
    context = {'form':form}
    return render(request,"auth/owner_register.html",context)

def login_customer(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.role == 0:
                messages.error(request,"Not registered as a customer!")
            else:
                login(request,user)
                return redirect("main:show_main")
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request,"auth/customer_login.html",context)

def register_customer(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 1
            user.save()
            return redirect("main:show_main")
    context = {'form':form,}
    return render(request,"auth/customer_register.html",context)

def logout_user(request):
    if request.user.is_authenticated:
        role = request.user.role
        logout(request)
        if role == 0:
            return redirect("main:login_owner")
        else:
            return redirect("main:login_customer")
    else:
        return redirect("main:show_main")
    