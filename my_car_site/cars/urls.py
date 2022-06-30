from django.urls import path
from .views import add, delete, list


app_name = 'cars'

urlpatterns = [
    path('list/', list, name='list'),
    path('delete/', delete, name='delete'),
    path('add/', add, name='add'),
]