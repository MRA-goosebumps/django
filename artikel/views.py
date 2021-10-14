from artikel.models import Artikel
#from django.shortcuts import render
from django.views.generic import ListView, DetailView


# Create your views here.
from .models import Artikel

class ArtikelListView(ListView):
    model = Artikel
    template_name = "artikel/artikel_list.html"
    context_object_name = 'artikel_list'

   
class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = "artikel/artikel_detail.html"
    context_object_name = 'artikel_detail'

