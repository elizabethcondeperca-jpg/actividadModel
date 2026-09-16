from django.shortcuts import render

# Create your views here.

from .models import Musician

def listado_albumes(request):
    musicos = Musician.objects.prefetch_related('album_set').all()
    return render(request, 'albumes.html', {'musicos': musicos})