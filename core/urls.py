from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from isar.views import index, transparencia, contato, noticias, sobreNos, noticia, governanca

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^$', index, name='home'),
    url(r'^sobre-nos$', sobreNos, name='sobre-nos'),
    url(r'^governanca$', governanca, name='governanca'),
    url(r'^transparencia$', transparencia, name='transparencia'),
    url(r'^contato$', contato, name='contato'),
    url(r'^noticias$', noticias, name='noticias'),
    url(r'^noticia/(?P<id>\d+)$', noticia, name='noticia'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
