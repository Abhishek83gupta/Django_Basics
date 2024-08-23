from django.urls import path
from . import views

# from .views import student


urlpatterns = [
    path('studentdata',views.student,name='static_data'),
    path('list', views.student_list, name='college_list'),
    path('create', views.save_student, name='create_college'),
]