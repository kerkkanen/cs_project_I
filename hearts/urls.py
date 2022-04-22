from django.urls import path

from .views import index, transfer, logout, find,delete, change

urlpatterns = [
    path('', index, name='index'),
    path('transfer/', transfer, name='transfer'),
    path('logout/', logout, name='logout'),
    path('find/', find, name='find'),
    path('delete/', delete, name='delete'),
    path('change/', change, name='change'),
   
    
    
]