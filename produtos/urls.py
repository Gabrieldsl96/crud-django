from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.produto_lista, name='lista'),
    path('criar/', views.produto_criar, name='criar'),
    path('<int:pk>/editar/', views.produto_editar, name='editar'),
    path('<int:pk>/deletar/', views.produto_deletar, name='deletar'),
]
