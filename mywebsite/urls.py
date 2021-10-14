from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('artikel/', include('artikel.urls', namespace='artikel')),
    path('', TemplateView.as_view(template_name = 'index.html'), name='home'),
    path('admin/', admin.site.urls),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

