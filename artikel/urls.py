from django.urls import path, re_path

from .views import (
    ArtikelListView, 
    ArtikelDetailView
)

urlpatterns = [
    re_path(r'^detail/(?P<slug>[\w-]+)/$', ArtikelDetailView.as_view(), name='detail'),
    path('', ArtikelListView.as_view(), name='list'),
    
]

app_name = 'artikel'

