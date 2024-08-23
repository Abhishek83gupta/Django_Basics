from django.urls import path
from . import views

urlpatterns = [
    path('list', views.company_list, name='college_list'),
    path('create', views.save_company, name='create_college'),
]