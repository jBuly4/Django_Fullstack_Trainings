from django.urls import path
# from .views import home_view
from .views import HomeView, ThankView
app_name = 'classroom'


# urlpatterns = [
#     path('', home_view, name='home'),  # path expects a function
# ]

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('thank_you/', ThankView.as_view(), name='thank_you'),
]