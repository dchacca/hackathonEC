from .models import Comisaria,Denuncia,Usuario
from rest_framework import serializers


class ComisariaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comisaria
        fields='__all__'

class DenunciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Denuncia
        fields='__all__'

    
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields='__all__'
        