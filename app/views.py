from django.shortcuts import render

# Create your views here.

def condition(request):
    d={'a':1000,'b':10,'c':2000000,'d':40,'e':200}
    return render(request,'condition.html',d)