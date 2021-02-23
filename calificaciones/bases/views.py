from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import *
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth.forms import UserCreationForm
from calificaciones.bases.forms import RegisterForm
from django import forms
from calificaciones.users.models import User
from django.contrib import messages
# Create your views here.
#def registeruser(request):
#    if request.method == 'POST':
#        form = RegisterForm(request.POST)
#        if form.is_valid():
#            form.save()
#            username = form.cleaned_data.get('username')
#            raw_password  = form.cleaned_data.get('password1')
#            user  = authenticate(username=username,password=raw_password)
#            login = (request,user)
#            return redirect('bases:home')
#        else:
#            form = RegisterForm()
#        return render(request,'register.html',{'form':form})

class SinPrivilegios(LoginRequiredMixin,PermissionRequiredMixin):
    login_url = 'bases:login'
    raise_exception = False
    redirect_field_name = "redirect_to"
    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user == AnonymousUser():
            self.login_url = 'bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class HomeSinPrivilegios(LoginRequiredMixin,TemplateView):
    login_url = "bases:login"
    template_name = "bases/sin_privilegios.html"

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('bases:home')

    else:
        form = AuthenticationForm()
    return render(request,'bases/login.html',{'form':form})

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "bases/login.html"
    success_url =  reverse_lazy("bases:home")
    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.success(self.request, 'Bienvenido')
        return super(LoginView, self).form_valid(form)


class UserNew(CreateView):
    model= User
    template_name="bases/register.html"
   
    form_class= RegisterForm
    success_url = reverse_lazy("bases:login")

    def get_context_data(self, **kwargs):
        context = super(UserNew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        print (form)
        if form.is_valid() :
            reg = form.save(commit=False)
            reg.is_active = False
            password = reg.dni

            reg.username = reg.dni
            #el set_password me sirve para poder cifrar la contraseña el mismo metodo que usa django
            reg.set_password(password)
            reg.save()
            print( reg.username,reg.password)
            print(request, "se creo ")
            messages.success(request , 'Registro con exito')
            return HttpResponseRedirect(self.get_success_url())
        else:
            #form = {
            #   'name':form.name,
            #   'apellido':form.apellido,
            #   'dni':form.dni,
            #   'phone':form.phone,
            #   'email':form.email,
            #   'date_of_birth':form.date_of_birth,
            #   'picture':form.picture
            #}
            
            return self.render_to_response(self.get_context_data(form=form))


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'
