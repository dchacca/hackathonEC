from .models import Comisaria,Denuncia,Denunciante
from rest_framework import serializers


class ComisariaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comisaria
        fields='__all__'

class DenunciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Denuncia
        fields='__all__'

    
class DenuncianteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Denunciante
        fields='__all__'
        