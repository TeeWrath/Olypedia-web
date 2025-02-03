from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def project(request):
    return render(request,'project.html')

def services(request):
    return render(request,'services.html')

def career(request):
    return render(request,'career.html')

def market(request):
    return render(request,'market.html')

def education(request):
    return render(request,'education.html')

def health(request):
    return render(request,'health.html')

def entertainment(request):
    return render(request,'entertainment.html')

def travel(request):
    return render(request,'travel.html')

def legal(request):
    return render(request,'legal.html')

def corporate(request):
    return render(request,'corporate.html')

def finance(request):
    return render(request,'finance.html')

