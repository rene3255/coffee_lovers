from django.shortcuts import render
from coffeehouse.models import CoffeeHouse
from django.db.models import Q


# Create your views here.


def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    coffees = CoffeeHouse.objects.filter(
                      Q(name__icontains=q) |
                      Q(city__icontains=q) |
                      Q(address__icontains=q)
                      )
                                         
                                         
    default_coffees = CoffeeHouse.objects.all()[:8]
    context = {'coffees': coffees, 'default_coffees': default_coffees}
    return render(request, 'pages/index.html', context)

         
 