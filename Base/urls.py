from django import views
from django.urls import path
from .views import BlogsDelete, BlogsCreacion, BlogsDetalle, BlogsLista, BlogsUpdate, LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword, HomeView, ComentarioPagina
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='base/logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),

    path('listaGuitarras/', BlogsLista.as_view(), name='guitarras'),

    path('blogDetalle/<int:pk>/', BlogsDetalle.as_view(), name='guitarra'),

    path('blogEdicion/<int:pk>/', BlogsUpdate.as_view(), name='guitarra_editar'),

    path('blogBorrado/<int:pk>/', BlogsDelete.as_view(), name='guitarra_eliminar'),

    path('blogCreacion/', BlogsCreacion.as_view(), name='nuevo'),

    path('blogDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    path('acercaDeMi/', views.about, name='acerca_de_mi'),
]
