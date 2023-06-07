from django.urls import path
from AAA.views import *

app_name='AAA'

urlpatterns=[
        path('alluarjun/',alluarjun,name='alluarjun')

]
