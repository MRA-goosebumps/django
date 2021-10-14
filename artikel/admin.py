from django.contrib import admin

# Register your models here.
from .models import Artikel

class ArtikelAdmin(admin.ModelAdmin):
    readonly_fields = [
        'published',
        'updated',
        'slug',
    ]

    search_fields = ('judul', 'kategori',)

admin.site.register(Artikel, ArtikelAdmin)
