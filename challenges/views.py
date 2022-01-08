from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month ",
    "february":  "valentine month",
    "march": "Learn django everday",
    "april":"Eat no meat for the entire month ",
    "may": "jog everyday",
    "june" : "Birthday month",
    "july" : "Eat no meat for the entire month ",
    "august": "Learn django everday",
    "september":"Eat no meat for the entire month ",
    "october": "jog everyday",
    "november" : "Eat no meat for the entire month ",
    "december": None,
}


# Create your views here.

def index(request):
    # list_items ="" 
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
       "months": months
    })
    

def monthly_challenge_by_number(request, month):
    months =list( monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('<h1>INVALID MONTH BABA<h1>')

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect (redirect_path)

    
  
def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return  render(request,"challenges/challenge.html", {
          "text": challenge_text,
           "month_name": month
        })
    except:
        raise Http404

        
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)














    # for month in months :
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li> <a href=\"{month_path} \">{capitalized_month}</a> </li>"
    

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)


    # return HttpResponseRedirect (f"/challenges/{redirect_month}" )


        # response_data = f"<h1>{challenge_text}</h1>"
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data) 

    # challenge_text = None
    # if month == "january":
    #     challenge_text = "SAPA MONTH!!!!"
    # elif month == "february":
    #     challenge_text="It's Valentine month!!!!"
    # elif month == "march":
    #     challenge_text= "new skill acquisistion!!!"
    # else:
    #     return HttpResponseNotFound('Not a supported month')

    # return HttpResponse(challenge_text)   