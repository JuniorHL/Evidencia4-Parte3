from ast import Return
import xdrlib
from django.shortcuts import render,HttpResponse
from requests import request
from miapp.models import Estudiante

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

def crear_estudiante(request):
    estudiante = Estudiante(
    codigo = "2013100093",
    dni = "7058514",
    nombre = "Luis",
    apepat = "Serna",
    apemat = "Malca",
    direccion = "Mz 162 H lote 6 -Los Angeles",
    telefono = "943251849",
    estado = "A",
    )
    estudiante.save()
    return HttpResponse (f"<h1>Estudiantes Registrados</h1>"+
    f"<br> <b>Codigo:</b> {estudiante.codigo} <br> <b>DNI:</b> {estudiante.dni} <br> <b>Nombre:</b> {estudiante.nombre}"+
    f"<br> <b>ApellidoPaterno:</b> {estudiante.apepat} <br> <b>ApellidoMaterno:</b> {estudiante.apemat} <br> <b>Direccion:</b> {estudiante.direccion}"+
    f"<br> <b>Telefono:</b> {estudiante.telefono} <br> <b>Estado:</b> {estudiante.estado}")
    