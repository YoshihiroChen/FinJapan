
from django.shortcuts import render

def investment_home(request):
    return render(request, 'investment/index.html')