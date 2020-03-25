from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Ejecutivo)
admin.site.register(Empresario)
admin.site.register(GeneroEscrito)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Ciudad)
admin.site.register(Sector)
admin.site.register(Periodicidad)
admin.site.register(TipoSociedad)
admin.site.register(PaisSociedad)
admin.site.register(Autor)
admin.site.register(Fuente)
admin.site.register(Sociedad)
admin.site.register(Propietario)
admin.site.register(PorcentajePropietario)
admin.site.register(Escrito)
admin.site.register(GeneroRadio)
admin.site.register(Radio)
admin.site.register(GeneroCanalTV)
admin.site.register(CanalTV)
admin.site.register(GeneroMedioDigital)
admin.site.register(MedioDigital)
admin.site.register(Cargo)
admin.site.register(CargoEjecutivo)
admin.site.register(TipoDocumento)
admin.site.register(Regulacion)