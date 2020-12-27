from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Produto, medida
from .forms import ProdutoForm


class ProdutoListView(ListView):
    model = Produto
    context_object_name = 'produtos'


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('Produto_changelist')


class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('Produto_changelist')


def load_cities(request):
    codigo_produto_id = request.GET.get('codigo_produto')
    cities = medida.objects.filter(codigo_produto_id=codigo_produto_id).order_by('name')
    return render(request, 'estoque/medida_dropdown_list_options.html', {'cities': cities})

def produto_remove(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    produto.delete()
    return redirect('Produto_changelist')

