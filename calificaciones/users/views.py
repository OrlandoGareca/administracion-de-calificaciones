from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render

from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView,ListView,CreateView,View
from calificaciones.bases.views import SinPrivilegios
from calificaciones.users.forms import RegistrationForm,UserCreationForm,UserChangeForm
from calificaciones.users.models import User
from django.contrib.auth.decorators import login_required,permission_required


class UserListView(SinPrivilegios,ListView):
    model = User
    template_name = "users/user_list.html"
    context_object_name = "obj"
    queryset = User.objects.order_by('id')
    permission_required ="users.user_view"


class UserNew(SinPrivilegios, CreateView):
    model= User
    template_name="users/user_new.html"
    context_object_name = "obj"
    form_class= UserCreationForm
    success_url = reverse_lazy("users:user_list")
    permission_required ="users.user_new"

class UserEdit(SinPrivilegios,UpdateView):
    model = User
    template_name = "users/register.html"
    context_object_name = "obj"
    form_class = UserCreationForm
    success_url = reverse_lazy("users:user_list")
    permission_required ="users.user_change"


@login_required(login_url="/login/")
@permission_required("users.user_change",login_url="/login/")
def UsuarioInactivar(request,id):
    user = User.objects.filter(pk=id).first()

    if request.method =="POST":
        if user:
            user.is_active = not user.is_active
            user.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    return HttpResponse("FAIL")




def perfil(request,id):
    template_name = 'users/porfile.html'

    print(id)
    obj = User.objects.get(id=id)
    print(obj)
    if request.method == 'GET':
        context = {"obj":obj}

    return render(request,template_name,context)
