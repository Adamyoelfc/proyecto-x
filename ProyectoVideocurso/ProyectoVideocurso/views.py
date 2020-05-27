from django.shortcuts import render
import datetime

def cursoC (request):

    fecha_actual = datetime.datetime.now()

    return render(request, "cursoC.html", {"dame_fecha" : fecha_actual })

def curso_css(request):
    
    fecha_actual = datetime.datetime.now()

    return render(request, 'cursoCss.html', {"dame_fecha" : fecha_actual})

    
    