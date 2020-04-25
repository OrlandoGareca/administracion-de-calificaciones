from django.urls import path

from calificaciones.users.views import (
    UserListView,
    UserNew,
    UserEdit,
    UsuarioInactivar,
    Porfile,
    perfil

)

app_name = "users"
urlpatterns = [

    path("",UserListView.as_view(),name='user_list'),
    path("create",UserNew.as_view(),name='user_new'),
    path('estado/<int:id>',UsuarioInactivar, name="user_inactivar"),
    path('porfile/<int:id>',perfil,name="user_perfil"),
    path("edit/<int:pk>",UserEdit.as_view(),name='user_edit'),
]

