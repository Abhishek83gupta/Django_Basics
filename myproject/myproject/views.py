from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
# from .models import Item
# from .forms import ItemForm 

# # Read (List all items)
# def item_list(request):
#     items = Item.objects.all()
#     return render(request, 'myapp/item_list.html', {'items': items})

def item_list(request):
    return JsonResponse({'message': 'hello', 'code': 200},status=200)

def chalo_browser(request):
    return JsonResponse({'message':'Bol Browser', 'code':200},status=200)

def item2(request):
    return JsonResponse({'name':'Pranav','Roll no': 14},status=200)