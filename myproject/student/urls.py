from django.urls import path
from . import views

# from .views import student


urlpatterns = [
    path('studentdata',views.student,name='static_data'),
    path('list', views.student_list, name='college_list'),
    path('create', views.save_student, name='create_college'),
    path('get_Student/<int:Student_id>',views.get_student,name='get_College'),
    path('update_Student/<int:Student_id>',views.update_student,name='update_College'),
    path('delete_Student/<int:Student_id>',views.delete_student,name='delete_College'),
]