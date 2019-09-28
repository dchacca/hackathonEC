
from django.urls import path,include
from . import views
from rest_framework import routers


router=routers.DefaultRouter()
router.register('comisaria',views.ComisariaView)
router.register('denuncia',views.DenunciaView)
router.register('denunciante',views.DenuncianteView)

urlpatterns = [
    path('',include(router.urls))
]
