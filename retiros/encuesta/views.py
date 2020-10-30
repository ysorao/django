from django.shortcuts import render, HttpResponse

# Create your views here.


def inicio(request):
    return render(request, "encuesta/encuesta.html")

def encuesta(request):
    return render(request, "encuesta/encuesta.html")

def pazysalvo(request):
    return render(request, "encuesta/pazysalvo.html")

def result(request):
    mensaje = "mensaje de respuesta"
    nombre= 'Yovanny'
    apellido='sora'
    context={
        'mensaje': mensaje,
        'nombre': nombre,
        'apellido': apellido,
    }   

    return render(request, "encuesta/result.html", context)

