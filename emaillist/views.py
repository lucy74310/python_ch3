from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from emaillist.models import Emaillist


def index(request):
    # id 컬럼 꺼꾸로
    emaillist = Emaillist.objects.all().order_by('-id')
    print(emaillist, type(emaillist))
    data = {'emaillist': emaillist}
    for t in emaillist:
        print(t, type(t))
    return render(request, 'emaillist/index.html', data)


def form(request):
    return render(request, 'emaillist/form.html')


def add(request):
    emaillist = Emaillist()
    
    emaillist.first_name = request.POST['fn']
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']
    
    emaillist.save()
    
    return render(request, 'emaillist/index.html')
