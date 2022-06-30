from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.


# def sports_view(request):
#     return HttpResponse("SPORTS PAGE")
#
#
# def finance_view(request):
#     return HttpResponse("FINANCE PAGE")

# dynamic views

articles = {
    'sports': 'SPORT PAGE',
    'finance': 'FINANCE PAGE',
    'politics': 'POLITICS PAGE'
}


def news_view(request, topic):
    try:
        response = articles[topic]
        return HttpResponse(response)
    except:
        # answer = "Not found that topic!"
        # return HttpResponseNotFound(answer)
        raise Http404("Generic error 404")


# def sum_view(request, num1, num2):
#     return HttpResponse(str(num1 + num2))

def sum_view(request, num1, num2):
    return HttpResponse(str(f"{num1} + {num2} = {num1 + num2}"))