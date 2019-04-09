#from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def referer_domain(request, code):
    return JsonResponse({'referer': request.META.get('HTTP_REFERER')})
