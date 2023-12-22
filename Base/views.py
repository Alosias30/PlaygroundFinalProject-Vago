from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Blog, Comentario
from .forms import ActualizacionBlog, FormularioCambioPassword, FormularioEdicion, FormularioNuevoBlog, FormularioRegistroUsuario, FormularioComentario


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'Base/home.html'

class LoginPagina(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

class RegistroPagina(FormView):
    template_name = 'base/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'base/edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'base/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'base/passwordExitoso.html', {})


# GUITARRA

class BlogsLista(LoginRequiredMixin, ListView):
    context_object_name = 'guitarras'
    queryset = Blog.objects.filter(instrumento__startswith='guitarra')
    template_name = 'Base/listaGuitarras.html'
    login_url = '/login/'

class BlogsDetalle(LoginRequiredMixin, DetailView):
    model = Blog
    context_object_name = 'guitarra'
    template_name = 'Base/blogDetalle.html'

class BlogsUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = ActualizacionBlog
    success_url = reverse_lazy('guitarras')
    context_object_name = 'guitarra'
    template_name = 'Base/blogEdicion.html'

class BlogsDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('guitarras')
    context_object_name = 'guitarra'
    template_name = 'Base/blogBorrado.html'

# CREACION INSTRUMENTO

class BlogsCreacion(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = FormularioNuevoBlog
    success_url = reverse_lazy('home')
    template_name = 'Base/blogCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BlogsCreacion, self).form_valid(form)

# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'Base/comentario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

# ACERCA DE MI

def about(request):
    return render(request, 'base/acercaDeMi.html', {})