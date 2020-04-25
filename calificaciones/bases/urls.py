from django.urls import include, path
from calificaciones.bases.views import *
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="bases/login.html"),name='logout'),
    path('register/',UserNew.as_view(),name="register"),
    path('sin_privilegios/',HomeSinPrivilegios.as_view(),name="sin_privilegios")
]
