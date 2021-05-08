from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import RequestContext, loader
# from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Person
from .models import Perform
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
from django.contrib.auth.decorators import login_required
@login_required(login_url='/accounts/login/')
def detail(request):
    peoples = Person.objects.all()
    return render(request,'main/main.html', locals())
@login_required(login_url='perform/')
def detail_perf(request):
    perf = Perform.objects.all()
    return render(request,'main/perform.html', locals())


