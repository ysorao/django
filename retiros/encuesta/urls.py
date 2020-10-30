from django.urls import path
from encuesta import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('encuesta', views.encuesta, name="Encuesta"),
    path('pazysalvo', views.pazysalvo)
   
]