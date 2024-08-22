from django.urls import path

from . import views

urlpatterns = [
    path('clgdata',views.college,name='getitem'),
    path('list', views.college_list, name='college_list'),
    path('create', views.save_college, name='create_college'),
    path('get_College/<int:College_id>',views.get_college,name='get_College'),
    path('update_College/<int:College_id>',views.update_college,name='update_College'),
    path('delete_College/<int:College_id>',views.delete_College,name='update_College'),
]