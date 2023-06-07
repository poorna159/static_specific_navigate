from django.urls import path
from sneha.views import *

app_name='sneha'

urlpatterns=[
        path('snehareddy/',snehareddy,name='snehareddy')

]
