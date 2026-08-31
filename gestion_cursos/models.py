from django.db import models


class Cursos(models.Model):
    '''
    Modelo que representa un proyecto
    '''
    titulo = models.CharField(max_length=100) #Un campo de texto osea un (Varchar)
    descripcion = models.TextField() #Campo de texto blanco
    nivel = models.CharField(max_length=13)

class Leccion(models.Model):
    '''
    modelo que representa la tarea de un proyecto
    '''

    ESTADO_CHOICES = [
        ('BORRADOR', 'Borrador'),
        ('PUBLICADO', 'Publicado'),
    ]
    
    # relacion 1 a muchos: un proyecto tiene muchas tareas
    curso = models.ForeignKey(
        Cursos,
        on_delete = models.CASCADE,
        related_name='lecciones',
    )
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=200)
    duracion = models.IntegerField()
    estado = models.CharField(
        max_length=9,
        choices= ESTADO_CHOICES,
        default='BORRADOR'
    )