from django.shortcuts import render

# Create your views here.

def kfu(request):
    return render(request,'kfu/kfu.html')