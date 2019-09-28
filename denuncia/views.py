from django.shortcuts import render
from rest_framework import viewsets
from .models import Comisaria,Denuncia,Denunciante
from .serializer import ComisariaSerializer,DenunciaSerializer,DenuncianteSerializer

class ComisariaView(viewsets.ModelViewSet):
    queryset=Comisaria.objects.all()
    serializer_class=ComisariaSerializer


class DenunciaView(viewsets.ModelViewSet):
    queryset=Denuncia.objects.all()
    serializer_class=DenunciaSerializer

class DenuncianteView(viewsets.ModelViewSet):
    queryset=Denunciante.objects.all()
    serializer_class=DenuncianteSerializer