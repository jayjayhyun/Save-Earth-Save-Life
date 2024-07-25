from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'index.html')
def blog(request):
    return render(request,'blog.html')
def blog_details(request):
    return render(request,'blog-details.html')
def service_details(request):
    return render(request,'service-details.html')
def starter_page(request):
    return render(request,'starter-page.html')