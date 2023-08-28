from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .forms import UsersForm

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
    if request.method == 'GET':
        name = request.GET.get('output')
        data = {
            'title': 'About Us',
            'name': name
        }
    return render(request, 'about.html', data)

def contactUs(request):
    print('request', request)
    fn = UsersForm()
    data={'form': fn}
    
    try:
        if request.method=='POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            data = {'name': name, 'email': email, 'subject':subject, 'message': message}
            # url = '/about-us?output={}'.format(name)
            # return redirect(url)
    except:
        pass

    return render(request, 'contact.html', data)

def courseDetail(request, courseId):
    return HttpResponse(f'course {courseId}')

def submitForm(request):
    name= ''
    if request.method == 'POST':
        name = request.POST.get('name')
    return HttpResponse(name)
