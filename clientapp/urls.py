from django.urls import path 
from .views import *


urlpatterns =[
    path('',index, name='client_index'),
    path('create',create_employee, name='create_employee')

]