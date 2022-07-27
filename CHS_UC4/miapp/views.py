from ast import Return
import xdrlib
from django.shortcuts import render,HttpResponse
from requests import request


# Create your views here.

layout =  """

                <h1> Evidencia 4 (LP3) | Serna , Huancas , Ccaccya <h1>
                <hr>


          """
def saludo(request):

    return render(request , 'saludo.html',{
        'titulo' : 'saludo',
        'saludo': 'Bienvenidos a la Evidencia IV'

    })
        
def integrantes(request):

    alumnos = [ 'Antony Ccaccya Huaman' ,
                    'Huancas Leuyacc Anselmo Junior',
                    'Serna Malca Luis Alejandro']

    return render(request, 'integrantes.html' , {
        
        'alumnos' : alumnos 
        
        })
    