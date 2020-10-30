from django.shortcuts import render, HttpResponse

# Create your views here.


def inicio(request):
    return render(request, "encuesta/encuesta.html")

def encuesta(request):
    return render(request, "encuesta/pazysalvo.html")

def pazysalvo(request):
    return render(request, "encuesta/pazysalvo.html")


