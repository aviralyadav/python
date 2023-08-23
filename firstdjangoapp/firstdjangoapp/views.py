from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def homePage(request):
    data = {
        'title': 'Home Page',
        'message': 'Welcome to Django',
        'clist': ['Php', 'JavaScript', 'Python'],
        'userDetail': [
            {'name': 'Aviral', 'mobile': '8496079312'},
            {'name': 'Abhishek', 'mobile': '8496072123'}
        ]
    }
    return render(request, "index.html", data)

def aboutUs(request):
    return HttpResponse('About US')

def course(request):
    return HttpResponse('Course')

def courseDetail(request, courseId):
    return HttpResponse(f'course {courseId}')
