from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
#def child1(request):
    #return render(request, 'base.html')

def trangchu(request):
    return render(request, 'base.html')

def child1(request):
    return render(request, 'child1.html')
