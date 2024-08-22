from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
# from .forms import ItemForm  # type: ignore

# Read (List all items)
def item_list(request):
    items = Item.objects.all()
    return render(request, 'myapp/item_list.html', {'items': items})