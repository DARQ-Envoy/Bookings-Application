from django.shortcuts import render, redirect
from .models import Booking
from django.contrib.auth.models import User as Business
from django.urls import  reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

def  homepage(request):
    is_authenticated = request.user.is_authenticated
    context = {"user_logged_in":is_authenticated}
    return render(request, "base_app/home.html",context)

@login_required(login_url=reverse_lazy("login"))
def dashboard(request):
    
    all_tables = Booking.objects.all()
    context = {"all_tables":all_tables}
    return render(request, "base_app/dashboard.html", context)


@login_required(login_url=reverse_lazy("login"))
def bookings(request):
    user = request.user
    #  I am intent on using the user object to access all bookings related to it.
    #  When you have internet connection later please uses the user object instead to fetch all 
    # booked_tables = 
    # context = {"booked_tables":booked_tables}
    context = {}
    return render(request, "base_app/bookings.html", context)
