from django.shortcuts import render

def category_list(request):
    data ={

    }
    return render(request, '../../template/category/list.html')