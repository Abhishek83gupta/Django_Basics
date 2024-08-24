from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Company
import json

def college(request):
    return JsonResponse({'name':'SCOE','address':'Kharghar'},status=200)

@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        college = list(Company.objects.values())
        return JsonResponse(college, safe=False)
    
    
@csrf_exempt
def save_company(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        company = Company.objects.create(
            name=data.get('company_name'),
            address=data.get('address'),
            phone_no=data.get('mobile_number'),
            company_type=data.get('company_type')
        )
        return JsonResponse({'id': company.id},status=201)    


# get specific data based on id
@csrf_exempt
def get_company(request,Company_id):
    if request.method == 'GET':
        print(Company_id)
        company_list = Company.objects.get(id=Company_id)
        data={
            'id':company_list.id,
            'name':company_list.name,
            'address':company_list.address,
            'phone_no':company_list.phone_no,
            'company_type':company_list.company_type,
        }
        return JsonResponse(data,safe=False)
    

@csrf_exempt
def update_company(request,Company_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        company_list = Company.objects.get(id=Company_id)
        company_list.name=data.get('name',company_list.name)
        company_list.address=data.get('address',company_list.address)
        company_list.phone_no=data.get('phone_no',company_list.phone_no)
        company_list.company_type=data.get('company_type',company_list.company_type)
        company_list.save()
        return JsonResponse({'id': company_list.id},status=201) 

# delete existing data    
@csrf_exempt
def delete_Company(request,Company_id):
    if request.method == 'DELETE':
      company_list = Company.objects.get(id=Company_id)
      company_list.delete()
      return JsonResponse({'id': company_list.id, 'message':"Company deleted succesfully"},status=201)    
