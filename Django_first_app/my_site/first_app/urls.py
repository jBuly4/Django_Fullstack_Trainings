from django.urls import path
from . import views


urlpatterns = [
    path('<str:topic>/', views.news_view),
    path('<int:num1>/<int:num2>/', views.sum_view),  # request first_app/numer1/number2/ will return sum of numbers
]