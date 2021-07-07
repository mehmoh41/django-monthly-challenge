from django.urls import path
from . import views

# above import means from the same directory import file views

urlpatterns = [
    path("" , views.index , name="challenges"),
    path("<int:month>" , views.monthly_challenge_by_number),
    path("<str:month>" , views.monthly_challenge , name="monthly-challenge")
];