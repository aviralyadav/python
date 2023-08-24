from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def homePage(request):
    data = {
        'title': 'Home Page',
        'message': 'Welcome to Django',
        'clist': ['Php', 'JavaScript', 'Python'],
        'numbers': [],
        'userDetail': [
            {'name': 'Aviral', 'mobile': '8496079312'},
            {'name': 'Abhishek', 'mobile': '8496072123'}
        ]
    }
    return render(request, "index.html", data)

def aboutUs(request):
    data = {
        'title': 'About Us'
    }
    return render(request, 'about.html', data)

def contactUs(request):
    data = {
        'title': 'Contact Us'
    }
    return render(request, 'contact.html')

def courseDetail(request, courseId):
    return HttpResponse(f'course {courseId}')
