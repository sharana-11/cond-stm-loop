from django.shortcuts import render

# Create your views here.
def if_demo(request):
    login=True
    return render(request,'if_demo.html',{'login':login})

def ifelse_demo(request):
    login=False
    return render(request,'ifelse_demo.html',{'login':login,'name':'Stark'})


def for_demo(request):
    return render(request,'for.html',{'items':['apple','ball','car']})