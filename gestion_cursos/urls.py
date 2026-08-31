from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('acerca-de/', views.acerda_de,name='acerca-de'),
    path('cursos/', views.cursos, name='cursos'),
    path('nuevo-curso/',views.nuevos_cursos,name='nuevos_cursos'),
    path('curso/<int:id>/', views.ver_curso, name='ver_curso'),
    path('curso/nuevo/', views.nuevo_curso,name='nuevo_curso'),
    path('curso/<int:id>/eliminar', views.eliminar_curso, name='eliminar_curso'),
    path('curso/<int:id>/editar', views.editar_curso, name='editar_curso'),
    path('curso/<int:curso_id>/leccion/nueva/', views.crear_leccion, name="crear_leccion"),
    path('leccion/<int:id>/avanzar',views.avanzar_estado_leccion, name='avanzar_estado_leccion'),
    path('leccion/<int:id>/avanzar',views.avanzar_rapido, name='avanzar_rapido'),
    path('leccion/<int:id>/eliminar',views.eliminar_leccion, name='eliminar_leccion'),
]