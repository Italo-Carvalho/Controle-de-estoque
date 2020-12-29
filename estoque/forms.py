from django import forms
from .models import Produto, medida


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('codigo_produto','medida','data_de_entrega','validade','quantidade')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medida'].queryset = medida.objects.none()

        if 'codigo_produto' in self.data:
            try:
                codigo_produto_id = int(self.data.get('codigo_produto'))
                self.fields['medida'].queryset = medida.objects.filter(codigo_produto_id=codigo_produto_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty medida queryset
        elif self.instance.pk:
            self.fields['medida'].queryset = self.instance.codigo_produto.medida_set.order_by('name')
