
from django.urls import path,include
from . import views
from rest_framework import routers


router=routers.DefaultRouter()
router.register('comisaria',views.ComisariaView)
router.register('denuncia',views.DenunciaView)
router.register('usuario',views.UsuarioView)

urlpatterns = [
    path('',include(router.urls))
]
