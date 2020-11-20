from django.shortcuts import render

def myfirstview(request):
    data={
        'name':'William'
    }

    return render(request,'index.html', data)
# Create your views here.
