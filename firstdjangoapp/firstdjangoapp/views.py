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
    print('request', request)
    data={}
    try:
        if request.method=='POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            data = {'name': name, 'email': email, 'subject':subject, 'message': message}
    except:
        pass

    return render(request, 'contact.html', data)

def courseDetail(request, courseId):
    return HttpResponse(f'course {courseId}')
