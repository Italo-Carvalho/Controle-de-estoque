from django.contrib import admin
from .models import codigo_produto, medida, Produto

admin.site.register(codigo_produto)
admin.site.register(medida)
admin.site.register(Produto)

