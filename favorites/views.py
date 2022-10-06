from django.shortcuts import render
from favorites.models import Favorite
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.

def favorites(request):
    context = {'context': 'Hello from favorites view'}
    return render(request, 'favorites.html', context)

def favorite_list(request, id, user):
    print("Si está autendicado")
    return render(request, 'favorites/favorite_list.html', context)