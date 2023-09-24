from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from .forms import JogosForm, MecanicaForm
from .models import Jogos, Mecanicas, Tables



# Create your views here.

@csrf_protect
def home(request):
    jogos = Jogos.objects.all()
    mecanicas = Mecanicas.objects.all()
    tables = Tables.objects.all()

  
    return render(request, "home.html", context = {"jogos": jogos, "mecanicas":mecanicas, "tables": tables})


def create_jogo(request):
  if request.method == 'POST':
      form = JogosForm(request.POST)
      if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
  else:
    form = JogosForm()
  return render(request, "formJogo.html", {"form": form} )

def update_jogo(request, pk):
  jogo = Jogos.objects.get(id = pk)
  form = JogosForm(instance = jogo)
  if request.method == 'POST':
      form = JogosForm(request.POST, instance=jogo)
      if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
        
  return render(request, "update_formJogo.html", {"form": form})

def create_mecanica(request):
  if request.method == 'POST':
      form = MecanicaForm(request.POST)
      if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
  else:
    form = MecanicaForm()
  return render(request, "formMecanica.html", {"form": form} )

def update_mecanica(request, pk):
  mecanica = Jogos.objects.get(id = pk)
  form = MecanicaForm(instance = mecanica)
  if request.method == 'POST':
      form = MecanicaForm(request.POST, instance=mecanica)
      if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
        
  return render(request, "update_formMecanica.html", {"form": form})

def delete_jogo(request, pk):
  return render(request, 'deleteJogo.html',)

def delete_mecanica(request, pk):
  return render(request, 'deleteMecanica.html',)