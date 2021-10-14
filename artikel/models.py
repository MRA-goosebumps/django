from django.db import models
from django.utils.text import slugify

# Create your models here.

class Artikel(models.Model):
    judul    = models.CharField(max_length= 255)
    isi      = models.TextField()
    KATEGORI = [
        ('Jurnal', 'Jurnal'),
        ('Berita', 'Berita'),
        ('Pengumuman', 'Pengumuman'),
        ('Ekstrakurikuler', 'Ekstrakurikuler'),
    ]
    kategori = models.CharField(max_length= 20, choices= KATEGORI)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)
    image = models.ImageField(null=True, blank=True)

    def save(self):
        self.slug = slugify(self.judul)
        super().save()

    def __str__(self):
        return "{}. {}".format(self.id, self.judul)
