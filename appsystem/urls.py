from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='Produto_changelist'), name='home'),
    path('estoque/', include('estoque.urls')),
    path('admin/', admin.site.urls),
]


