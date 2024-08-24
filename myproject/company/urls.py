from django.urls import path
from . import views

urlpatterns = [
    path('list', views.company_list, name='college_list'),
    path('create', views.save_company, name='create_college'),
    path('get_Company/<int:Company_id>',views.get_company,name='get_College'),
    path('update_Company/<int:Company_id>',views.update_company,name='update_College'),
    path('delete_Company/<int:Company_id>',views.delete_Company,name='delete_College'),
]