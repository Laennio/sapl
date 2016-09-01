from django.conf.urls import include, url
from django.contrib.auth import views
from django.views.generic.base import TemplateView

from .apps import AppConfig
from .forms import LoginForm
from .views import (CasaLegislativaCrud, HelpView,
                    RelatorioMateriasPorAnoAutorTipoView,
                    RelatorioMateriasPorAutorView)

app_name = AppConfig.name


urlpatterns = [
    url(r'^sistema/', TemplateView.as_view(template_name='sistema.html')),
    url(r'^ajuda/', TemplateView.as_view(template_name='ajuda.html')),
    url(r'^relatorios/', TemplateView.as_view(
        template_name='base/relatorios_list.html')),
    url(r'^ajuda/(?P<topic>\w+)$', HelpView.as_view(), name='help_topic'),
    url(r'^ajuda/', TemplateView.as_view(template_name='ajuda/index.html'),
        name='help_base'),
    url(r'^casa_legislativa/', include(CasaLegislativaCrud.get_urls())),

    url(r'^login/$', views.login, {
        'template_name': 'base/login.html', 'authentication_form': LoginForm},
        name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}, name='logout'),

    url(r'^relatorio/materia-por-autor$',
        RelatorioMateriasPorAutorView.as_view(), name='materia_por_autor'),
    url(r'^relatorio/materia-por-ano-autor-tipo$',
        RelatorioMateriasPorAnoAutorTipoView.as_view(),
        name='materia_por_ano_autor_tipo'),
]
