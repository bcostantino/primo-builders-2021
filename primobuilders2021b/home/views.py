from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def services(request):
    return render(request, 'home/services.html')

def areasOfServ(request):
    return render(request, 'home/areasOfServ.html')

def consultation(request):
    return render(request, 'home/consultation')
