from django.shortcuts import render


def index(request):
    return render(request, 'investment/index.html')


def cash(request):
    return render(request, 'investment/cash.html')


def etf(request):
    return render(request, 'investment/etf.html')


def reit(request):
    return render(request, 'investment/reit.html')


def stocks(request):
    return render(request, 'investment/stocks.html')


def crypto(request):
    return render(request, 'investment/crypto.html')