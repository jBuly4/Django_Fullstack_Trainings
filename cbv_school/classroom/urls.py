from django.urls import path
# from .views import home_view
from .views import (HomeView, ThankView,
                    ContactFormView, TeacherCreateView,
                    TeacherListView, TeacherDetailView,
                    TeacherUdpateView)
app_name = 'classroom'


# urlpatterns = [
#     path('', home_view, name='home'),  # path expects a function
# ]

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('thank_you/', ThankView.as_view(), name='thank_you'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('create_teacher/', TeacherCreateView.as_view(), name='create_teacher'),
    path('list_teacher/', TeacherListView.as_view(), name='list_teacher'),
    path('teacher_detail/<int:pk>', TeacherDetailView.as_view(), name='detail_teacher'),  # to gain specific teacher
    # using its PK
    path('update_teacher/<int:pk>', TeacherUdpateView.as_view(), name='update_teacher'),

]
