from django.urls import path
from . import views

urlpatterns = [
    path('cust',views.cust_pageone,name='pageone'),
]