from django.forms import ModelForm
from appdobahamut.models import Jogos,Mecanicas


class JogosForm(ModelForm):
    class Meta:
        model = Jogos
        fields = ["tittle", "director", "mainProgrammer", "producer"]


form = JogosForm()

class MecanicaForm(ModelForm):
  class Meta:
        model = Mecanicas
        fields = ["tittle", "discription", "howMuchILike"]


form = MecanicaForm()