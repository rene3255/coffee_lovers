from django.shortcuts import render
from coffeehouse.models import CoffeeHouse
from django.db.models import Q

# Create your views here.

def coffeehouse(request):
    context={'context': 'Helllo from Coffeehouse view'}
    return render(request, 'coffeehouse/coffeehouse.html',context)

def coffee_detail(request, id):
    detail_result_set = CoffeeHouse.objects.filter(id=id)
    context = {'coffee_details': detail_result_set}
    return render(request, 'coffeehouse/coffee_details.html',context)
  
