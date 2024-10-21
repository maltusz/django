from django.contrib import admin
from django.urls import path
from procedimentos.views import index, listar, adicionar, editar
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', index, name='index'),
    path('listar/', listar),
    path('adicionar/', adicionar),
    path('editar/<int:id>/', editar)
]

