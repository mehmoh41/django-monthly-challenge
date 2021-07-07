from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse
monthly_challenges = {
    "january" : "Be careful to have a good start of the year.",
    "febraury": "Every year's febraury month is very special month.",
    "march"   : "March is month of peace and harmony.",
    "april"   : "April is month of men",
    "may"     : "May is month of those who tries hard",
    "june"    : "june is month when the country tournaments starts",
    "july"    : "start of the july is the end of tournaments",
    "august"  : "august is month when some counteries got their independent",
    "september" : "month of honour and pride",
    "october"  : "month of being men and preparing for cold weather",
    "november" : None, 
    "december" : "the last month of the year",
    
}

# Create your views here.

def index(request) : 
   
    months =  list(monthly_challenges.keys())
    return render(request , "challenges/index.html" , {
        "months" : months
    })


def monthly_challenge_by_number(request , month):
    months =  list(monthly_challenges.keys())

    if month > len(months): 
        return HttpResponseNotFound("Month not found")
    
    
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly-challenge",args=[redirect_month]) #challenges/monthName
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request , month): 
    try: 
        challenge_text = monthly_challenges[month]
        return render(request , "challenges/challenge.html" , {
            "text": challenge_text,
            "month": month,
        })
    except: 
        raise Http404()
    