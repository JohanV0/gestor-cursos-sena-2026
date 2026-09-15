from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from . models import Cursos, Leccion

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def acerda_de(request):
    return render(request,'acerca-de.html')

@login_required
def cursos(request):
    cursos = Cursos.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

@login_required
def nuevos_cursos(request):
    Cursos.objects.create(
    Titulo="JavaScript", 
    descripcion="Curso Basico de JavaScript", 
    nivel='principiante'
    )
    return HttpResponse('registro guardado')

@login_required
def ver_curso (request,id):
    curso = Cursos.objects.get(id=id)
    return render(request, 'detalle-curso.html',{'curso' : curso})

@login_required
def nuevo_curso(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        nivel = request.POST.get('nivel')
    
        if titulo and descripcion and nivel: 
            curso = Cursos(
                titulo=titulo,
                descripcion=descripcion,
                nivel=nivel
            )
            curso.save()

            return redirect('cursos')

    return render(request, 'nuevos_cursos.html')

@login_required
def eliminar_curso(request,id):
    curso = Cursos.objects.get(id=id)
    curso.delete()
    return redirect('cursos')

@login_required
def editar_curso(request,id):
    curso = Cursos.objects.get(id=id)
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        nivel = request.POST.get('nivel')

        if titulo and descripcion and nivel:
            curso.titulo = titulo
            curso.descripcion = descripcion
            curso.nivel = nivel
            curso.save()
            return redirect('ver_curso',id=curso.id)
        
    return render(request, 'editar-curso.html', {"curso":curso})

@login_required
def crear_leccion(request,  curso_id):
    curso = get_object_or_404(Cursos, id=curso_id)

    if request.method == 'POST':
        titulo = request.POST.get('titulo').strip()
        contenido = request.POST.get('contenido')
        duracion = request.POST.get('duracion')
        estado = request.POST.get('estado')

        if titulo:
            leccion = Leccion(
                titulo=titulo,
                contenido=contenido,
                duracion=int(duracion),
                estado=estado,
                curso=curso)
            leccion.save()

            return redirect('ver_curso', id=curso_id)
    
    datos = {
        'curso' : curso,
        'estado_choices': Leccion.ESTADO_CHOICES
    }

    return render(request,'crear_leccion.html', datos)

#lo siguiente es un decorador, le da indicaciones a lo que esta debajo de el, ya sea metodo u otra cosa

@require_POST
def avanzar_estado_leccion(request, id):
    leccion = get_object_or_404(Leccion, id=id)

    if leccion.estado == 'BORRADOR':
        leccion.estado = 'PUBLICADO'
        leccion.save()
    
    return redirect('ver_curso', id=leccion.curso.id)

def avanzar_rapido(request,id):
    leccion = get_object_or_404(Leccion, id=id)
    
    if leccion.estado != 'PUBLICADO':
        leccion.estado = 'PUBLICADO'
        leccion.save()
    
    return redirect('ver_curso', id=leccion.curso.id)

@require_POST
def eliminar_leccion(request,id):
    leccion = get_object_or_404(Leccion,id=id)
    id_curso = leccion.curso.id
    leccion.delete()
    return redirect('ver_curso',id=id_curso)
