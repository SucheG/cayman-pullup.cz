from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import Osoba, hashids
from django.shortcuts import redirect, get_object_or_404

class Index(ListView):
  context_object_name = 'osoby'
  queryset = Osoba.objects.filter(trener=True)
  template_name = 'letadlo/index.html'

def materialy(request, hashid):
  pk = hashids.decode(hashid)
  pocet = Osoba.objects.filter(pk=pk).count()
  if not pocet:
    return redirect(Index)

  return HttpResponse('materialy')

def edit(request, hashid, attr, value):
  pk = hashids.decode(hashid)
  osoba = get_object_or_404(Osoba, pk=pk)

  return HttpResponse('edit')

