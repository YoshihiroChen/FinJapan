from django.shortcuts import render


def guide(request):
    return render(request, "investment_system/guide.html")


def nisa(request):
    return render(request, "investment_system/nisa.html")


def ideco(request):
    return render(request, "investment_system/ideco.html")


def pension(request):
    return render(request, "investment_system/pension.html")
