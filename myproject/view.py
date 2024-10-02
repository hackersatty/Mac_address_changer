#from django.http import HttpResponse

from django.shortcuts import render

def Homepage(request):
    #return HttpResponse("Hello World , hackersatty here")
    return render(request, 'home.html')
def about(request):
    #return HttpResponse("This is about page")
    return render(request, 'About.html')