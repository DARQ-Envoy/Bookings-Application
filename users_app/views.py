from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User as Business
from .forms import User_Login_Form, User_Signup_Form

# Create your views here.




def user_signup(request):
    user = request.user
    form = User_Signup_Form()
    if user.is_authenticated:
        redirect("dashboard")
    if request.method == "POST":
        data = request.POST
        form_data = User_Signup_Form(data)
        if form_data.is_valid():
            user = form_data.save(commit=False)
            user.set_password(form_data.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect(reverse("dashboard"))
        else:
            form.add_error(None, "Username is invalid")
    context = {"form":form, "to_login":False}
    return render(request, "users_app/user_auth.html", context)




def user_login(request):
    user = request.user
    form = User_Login_Form()
    # print(form)
    if user.is_authenticated:
        redirect("dashboard")
    if request.method == "POST":
        data = request.POST
        form_data = User_Login_Form(data)
        # print(form_data, dir(form_data))
        if form_data.is_valid():
            user = authenticate(request, username = form_data.cleaned_data["username"], password = form_data.cleaned_data["password"])

            if user is not None:
                login(request,user)
                return redirect(reverse("dashboard"))
            else:
                form_data.add_error(None,"Incorrect email or password")
                

    context = {"form":form, "to_login":True}
    return render(request, "users_app/user_auth.html", context)


@login_required(login_url=reverse_lazy("login"))
def user_logout(request):
    logout(request)
    return redirect(reverse("homepage"))