from django.urls import path
from . import views

app_name = 'favorites'
urlpatterns=[
        path('', views.favorites,name='favorites'),
        path('favorite/<int:id>/<str:name>',views.favorite_list,name='favorite'),
    ]
