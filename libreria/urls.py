from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path("",views.inicio,name="inicio"),
    path("nosotros",views.nosotros,name="nosotros"),
    path("libros",views.libros, name="libros"),
    path("libros/crear",views.crear_libro,name="crear"),
    path("libros/editar",views.editar_libro,name="editar"),
    path("libros/eliminar/<int:id>",views.borrar_libro,name="borrar"),
    path("libros/editar/<int:id>",views.editar_libro,name="editar")
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)