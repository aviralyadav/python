from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def homePage(request):
    return render(request, "index.html")

def aboutUs(request):
    return HttpResponse('About US')

def course(request):
    return HttpResponse('Course')

def courseDetail(request, courseId):
    return HttpResponse(f'course {courseId}')
