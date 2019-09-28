from django.shortcuts import render
from rest_framework import viewsets
from .models import Comisaria,Denuncia,Usuario
from .serializer import ComisariaSerializer,DenunciaSerializer,UsuarioSerializer

class ComisariaView(viewsets.ModelViewSet):
    queryset = Comisaria.objects.all()
    serializer_class=ComisariaSerializer


class DenunciaView(viewsets.ModelViewSet):
    queryset = Denuncia.objects.all()
    serializer_class=DenunciaSerializer

class UsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class=UsuarioSerializer