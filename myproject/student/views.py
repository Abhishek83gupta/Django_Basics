from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import STUDENT
import json
# Create your views here.

def student(request):
    return JsonResponse({'name':'Abhishek',
                         'rollno':'15', 
                         'branch':'IT',
                         'frindes':["Pranav", "Prasad", "Nikhil", "Sahil", "Sujata", "Gauri"]
                         },status=200)

@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        # student = list(STUDENT.objects.values())
        # Student_list = list(Student.objects.select_related('college_id').values())
        Student_list = list(STUDENT.objects.values(
            'id', 'name', 'address', 'number', 'college_id', 'collegename', 'collegeaddress', 'college_mobileNumber'))
        print(Student_list)
        return JsonResponse(student, safe=False)
    
@csrf_exempt
def save_student(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        student = STUDENT.objects.create(
            name=data.get('name'),
            address=data.get('address'),
            phone_no=data.get('mobile_number'),
            college_name=data.get('clg_name'),
            college = student
        )
        return JsonResponse({'id': student.id},status=201)    
    










    

# @csrf_exempt
# def Student_list(request):
#     if request.method == 'GET':
#         # Student_list = list(Student.objects.values())
#         # Student_list = list(Student.objects.select_related('college_id').values())
#         Student_list = list(Student.objects.values(
#             'id', 'name', 'address', 'number', 'college_id', 'collegename', 'collegeaddress', 'college_mobileNumber'))
#         print(Student_list)
#         return JsonResponse(Student_list, safe=False)


# @csrf_exempt
# def save_student(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         getCollege = collage.objects.get(id=data.get('college'))
#         createStudnet = Student.objects.create(
#             name =data.get('name'),
#             address = data.get('address'),
#             number=data.get('number'),
#             college =getCollege
#         )
#         return JsonResponse({'id': createStudnet.id}, status=201)    
