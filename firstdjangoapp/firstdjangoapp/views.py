from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .forms import UsersForm
from services.models import Services
from neww.models import Neww
from django.core.paginator import Paginator
from contact_enquiry.models import ContactEnquiry

def homePage(request):
    newsData = Neww.objects.all()
    servicesData=Services.objects.all().order_by('-service_title')
    # use - dash for descending order, by default it will take ascending
    data = {
        'title': 'Home Page',
        'message': 'Welcome to Django',
        'clist': ['Php', 'JavaScript', 'Python'],
        'numbers': [],
        'userDetail': [
            {'name': 'Aviral', 'mobile': '8496079312'},
            {'name': 'Abhishek', 'mobile': '8496072123'}
        ],
        'servicesData':servicesData,
        'newsData': newsData
    }
    return render(request, "index.html", data)

def services(request):
    # __icontains  for filtering with like %name%
    servicesData=Services.objects.all()
    paginator = Paginator(servicesData, 1)
    page_number = request.GET.get('page')
    servicesData_final = paginator.get_page(page_number)
    total_page = servicesData_final.paginator.num_pages
    # if request.method == 'GET':
    #     sn=request.GET.get('servicename')
    #     if sn!= None:
    #         servicesData=Services.objects.filter(service_title__icontains=sn)
    data = {
        'servicesData': servicesData_final,
        'total_page': total_page,
        'pages_list': [n+1 for n in range(total_page)]
    }
    return render(request, 'services.html', data)

def newsDetail(request, newsslug):
    newsDetail = Neww.objects.get(news_slug=newsslug)
    return render(request, 'news-detail.html', {'newsDetail': newsDetail})

def aboutUs(request):
    if request.method == 'GET':
        name = request.GET.get('output')
        data = {
            'title': 'About Us',
            'name': name
        }
    return render(request, 'about.html', data)

def calculator(request):
    c=''
    num1 = ''
    num2 = ''
    if request.POST.get('num1') == '':
                return render(request, 'calculator.html', {'error':True})
    try:
        if request.method == 'POST':
            num1 = eval(request.POST.get('num1'))
            num2 = eval(request.POST.get('num2'))
            
            opr = request.POST.get('opr')
            if opr == '+':
                c = num1+num2
            elif opr == '-':
                c = num1-num2
            elif opr == '*':
                c = num1*num2
            else:
                c = num1/num2
    except:
        c = 'invalid opration'
    print(c)

    return render(request, 'calculator.html', {'num1':num1, 'num2': num2, 'output': c})

def saveEnquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        form = ContactEnquiry(name=name, email=email, subject=subject, message=message)
        form.save()
    return render(request, 'contact.html')

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
