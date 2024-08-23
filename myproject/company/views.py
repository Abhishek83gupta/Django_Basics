from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Company
import json

def college(request):
    return JsonResponse({'name':'SCOE','address':'Kharghar'},status=200)

# GET Api
@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        company = list(Company.objects.values())
        return JsonResponse(company, safe=False)
    
# Post Api   
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
                            