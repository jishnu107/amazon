from django.shortcuts import render

# Create your views here.

def cust_pageone(request):
    return render(request,'cust/pageone.html')