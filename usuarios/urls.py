from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.usuario_lista, name='lista'),
    path('criar/', views.usuario_criar, name='criar'),
    path('<int:pk>/editar/', views.usuario_editar, name='editar'),
    path('<int:pk>/deletar/', views.usuario_deletar, name='deletar'),
]
