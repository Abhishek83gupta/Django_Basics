from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myproject.serializers import CollegeSerializer
from .models import College
import json


# get all data
@csrf_exempt
def college_list(request):
    if request.method == 'GET':
        college = list(College.objects.values())
        return JsonResponse(college, safe=False)
    
# add new data    
@csrf_exempt
def save_college(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = CollegeSerializer(data=data)
        if serializer.is_valid():
           college = College.objects.create(
             collage_name=data.get('collage_name'),
             address=data.get('address'),
             phone_no=data.get('phone_no')
            )
        return JsonResponse({'id': college.id},status=201)    
    return JsonResponse(serializer.errors,status=400)
    
# get specific data based on id
@csrf_exempt
def get_college(request,College_id):
    if request.method == 'GET':
        print(College_id)
        collage_list = College.objects.get(id=College_id)
        data={
            'id':collage_list.id,
            'name':collage_list.collage_name,
            'address':collage_list.address,
            'phone_no':collage_list.phone_no,
        }
        return JsonResponse(data,safe=False)    
    
                                
# update existing data
@csrf_exempt
def update_college(request,College_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        collage_list = College.objects.get(id=College_id)
        collage_list.collage_name=data.get('collage_name',collage_list.collage_name)
        collage_list.address=data.get('address',collage_list.address)
        collage_list.phone_no=data.get('phone_no',collage_list.phone_no)
        collage_list.save()
        return JsonResponse({'id': collage_list.id},status=201)
    

# delete existing data    
@csrf_exempt
def delete_College(request,College_id):
    if request.method == 'DELETE':
      college_list = college.objects.get(id=College_id)
      college_list.delete()
      return JsonResponse({'id': college_list.id, 'message':"College deleted succesfully"},status=201)
                            
def college(request):
    return JsonResponse({'name':'SCOE','address':'Kharghar'},status=200)