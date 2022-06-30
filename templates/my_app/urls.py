from django.urls import path
from . import views

# register the app namespace URL NAMES
app_name = 'my_app'  # for using in redirects. it is special name for django. should be the same

# urlpatterns = [
#     path('', views.example_view),
#     path('variable/', views.variable_view),
# ]

urlpatterns = [
    path('', views.example_view, name='example'),
    path('variable/', views.variable_view, name='variable'),
]

# we can use url-tag {% url 'my_app:name' %} to create links on pages. value for name is example or variable for this
# case
# if you want to redirect in urls.py on project level then remove my_app: before name