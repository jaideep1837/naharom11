from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    
    n1 = str(request.POST.get('num1'))
    n2 = str(request.POST.get('num2'))
    n3 = str(request.POST.get('gender'))
    n4 = str(request.POST.get('num4'))
    if n1!="" and n2!="None" and n3!="Select" and n4!="Skills":     
        with open("data.txt",'a') as f:
            f.write(n1+','+n2+','+n3+','+n4+'\n')
    
    return render(request,'index.html')