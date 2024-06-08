from django.urls import path
from .views import homepage, dashboard, bookings

urlpatterns = [
    path("", homepage, name="homepage"),
    path("dashboard/", dashboard, name="dashboard"),
    path("bookings/",bookings,name="bookings")
]