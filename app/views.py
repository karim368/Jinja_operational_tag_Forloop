from django.shortcuts import render

# Create your views here.

def forloop(request):
    d = {'name':'Karim','numbers':(1,2,3,4,5,6,7,8,9,10)}
    return render(request,'forloop.html',d)