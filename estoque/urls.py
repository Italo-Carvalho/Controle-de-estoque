from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.ProdutoListView.as_view(), name='Produto_changelist'),
    path('add/', views.ProdutoCreateView.as_view(), name='Produto_add'),
    path('<int:pk>/', views.ProdutoUpdateView.as_view(), name='Produto_change'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('<int:pk>/remove/', views.produto_remove, name='produto_remove')
]
