from django.shortcuts import render

# Create your views here.

def data_render(request):
    d={'name':'PRITAM','age':23}
    return render(request, 'data_render.html', context=d)

def condition(request):
    dict={'a':1000,'b':200, 'c':300}
    return render(request, 'condition.html', context=dict)