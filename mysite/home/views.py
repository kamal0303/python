from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    context = {
        "variable1": "this is sent",
        "variable2": "welcome to the jungle"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is Homepage")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")


def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")


def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")
