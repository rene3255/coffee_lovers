from django.urls import path
from . import views

app_name = 'coffeehouse'
urlpatterns = [
    path('', views.coffeehouse,name='coffee'),
    path('details/<int:id>', views.coffee_detail,name='details'),
]