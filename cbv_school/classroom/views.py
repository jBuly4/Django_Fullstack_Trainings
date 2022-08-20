from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


# def home_view(request):
#     return render(request, 'classroom/home.html')


class HomeView(TemplateView):
    template_name = 'classroom/home.html'  # that's enough to render template


class ThankView(TemplateView):
    template_name = 'classroom/thank_you.html'

# TemplateViews should be used in cases where all work will be done inside template