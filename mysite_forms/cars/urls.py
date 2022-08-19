from django.urls import path
from .views import rental_review, thank_you


app_name = 'cars'


urlpatterns = [
    path('rental_review/', rental_review, name='rental_review'),
    path('thank_you/', thank_you, name='thank_you'),
]

"""
After we created project and prepared templates, urls and simple views, then we need to create forms.
In templates we need to print tags forms with method and label. Then we need to create cars/forms.py, create django 
class for forms. After that in templates we will use csrf tags and tag {{ form }}.
"""