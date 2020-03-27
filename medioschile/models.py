from django.db import models

# Create your models here.

from django.db import models
import datetime
YEAR_CHOICES = []
for r in range(1900, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))
# Create your models here.


class Ejecutivo(models.Model):
	class Meta:
			verbose_name = 'Ejecutivo de Medio'
			verbose_name_plural = 'Ejecutivos de Medios'
	ejecutivo = models.CharField("Ejecutivo", max_length=255, unique=True)
	def __unicode__(self):
		return self.ejecutivo

class Empresario(models.Model):
	class Meta:
			verbose_name = 'Miembro Directorio'
			verbose_name_plural = 'Miembros de Directorios'
	empresario = models.CharField("Miembro de Directorio", max_length=255, unique=True)
	def __unicode__(self):
		return self.empresario

class GeneroEscrito(models.Model):
	class Meta:
			verbose_name = 'Género Medio Escrito'
			verbose_name_plural = 'Géneros Medios Escritos'
	genero = models.CharField("Género", max_length=255, unique=True)
	def __unicode__(self):
		return self.genero

class Region(models.Model):
	class Meta:
			verbose_name = 'Región'
			verbose_name_plural = 'Regiones'
	region = models.CharField("Región", max_length=255, unique=True)
	def __unicode__(self):
		return self.region

class Comuna(models.Model):
	class Meta:
			verbose_name = 'Comuna'
			verbose_name_plural = 'Comunas'
	comuna = models.CharField("Comuna", max_length=255, unique=True)
	def __unicode__(self):
		return self.comuna

class Ciudad(models.Model):
	class Meta:
			verbose_name = 'Ciudad'
			verbose_name_plural = 'Ciudades'
	ciudad = models.CharField("Ciudad", max_length=255, unique=True)
	def __unicode__(self):
		return self.ciudad

class Sector(models.Model):
	class Meta:
			verbose_name = 'Sector de Actividad Socio'
			verbose_name_plural = 'Sectores de Actividad Socios'
	sector = models.CharField("Sector de Actividad Socios", max_length=255, unique=True)
	def __unicode__(self):
		return self.sector

class Periodicidad(models.Model):
	class Meta:
			verbose_name = 'Periodicidad'
			verbose_name_plural = 'Periodicidades'
	periodicidad = models.CharField("Periodicidad", max_length=255, unique=True)
	def __unicode__(self):
		return self.periodicidad

class TipoSociedad(models.Model):
	class Meta:
			verbose_name = 'Tipo Sociedad'
			verbose_name_plural = 'Tipos de Sociedades'
	tiposociedad = models.CharField("Tipo Sociedad", max_length=255, unique=True)
	def __unicode__(self):
		return self.tiposociedad

class PaisSociedad(models.Model):
	class Meta:
			verbose_name = 'País'
			verbose_name_plural = 'Paises'
	paissociedad = models.CharField("Pais", max_length=255, unique=True)
	def __unicode__(self):
		return self.paissociedad

class Autor(models.Model):
	class Meta:
			verbose_name = 'Autor'
			verbose_name_plural = 'Autores'
	autor = models.CharField("Autor", max_length=255, unique=True)
	def __unicode__(self):
		return self.autor
	datosautor = models.CharField("Datos Autor", max_length=255, null=True, blank=True)

class Fuente(models.Model):
	class Meta:
			verbose_name = 'Fuente'
			verbose_name_plural = 'Fuentes'
	fuente = models.CharField("Fuente", max_length=255, unique=True)
	def __unicode__(self):
		return self.fuente
	descripcionfuente = models.TextField("Descripción", null=True, blank=True)
	autor = models.ManyToManyField(Autor, verbose_name="Autor/es", blank=True, help_text="Actualice con F5")
	linkfuente = models.URLField("Link", null=True, blank=True, help_text="http://...")

class Sociedad(models.Model):
	class Meta:
			verbose_name = 'Socio'
			verbose_name_plural = 'Socios'
	sociedad = models.CharField("Socio", max_length=255, unique=True)
	def __unicode__(self):
		return self.sociedad
	rutsociedad = models.CharField("R.U.T.", max_length=255, null=True, blank=True)
	tiposociedad = models.ForeignKey(TipoSociedad, verbose_name="Tipo de Sociedad", related_name="sociedad_tiposociedad", null=True, blank=True, on_delete=models.PROTECT)
	paissocio = models.ForeignKey(PaisSociedad, related_name="pais_socio", verbose_name="País de origen", null=True, blank=True, on_delete=models.PROTECT)
	controlador = models.ForeignKey('self', related_name="controlador_socio", verbose_name="Controlador", null=True, blank=True, on_delete=models.PROTECT)
	presidentedirectorio = models.ForeignKey(Empresario, related_name="sociedad_presidentedirectorio", verbose_name="Presidente Directorio", null=True, blank=True, on_delete=models.PROTECT)
	miembrosdirectorio = models.ManyToManyField(Empresario, related_name="sociedad_miembrosdirectorio", verbose_name="Miembros Directorio", blank=True, help_text="Actualice con F5")
	utilidades = models.CharField("Utilidades -último año-", max_length=255, null=True, blank=True)
	infoutilidades = models.CharField("Información Utilidades", max_length=255, null=True, blank=True)
	fuenteutilidades = models.ForeignKey(Fuente, related_name="fuente_utilidades_sociedad", verbose_name="Fuente", null=True, blank=True, max_length=255, on_delete=models.PROTECT)
	sectores = models.ManyToManyField(Sector, verbose_name="Sectores de Actividad Socio", blank=True, help_text="Actualice con F5")
	fuentesociedad = models.ForeignKey(Fuente, verbose_name="Fuente", null=True, blank=True, max_length=255, on_delete=models.PROTECT)

class Propietario(models.Model):
	class Meta:
			verbose_name = 'Empresa/Sociedad Controladora'
			verbose_name_plural = 'Empresas/Sociedades Controladoras'
	propietario = models.CharField("Empresa/Sociedad Controladora", max_length=255, unique=True)
	def __unicode__(self):
		return self.propietario
	rutpropietario = models.CharField("R.U.T.", max_length=255, null=True, blank=True)
	tiposociedad = models.ForeignKey(TipoSociedad, verbose_name="Tipo de Sociedad", related_name="propietario_tiposociedad", null=True, blank=True, on_delete=models.PROTECT)
	presidentedirectorio = models.ForeignKey(Empresario, related_name="propietario_presidentedirectorio", verbose_name="Presidente Directorio", null=True, blank=True, on_delete=models.PROTECT)
	miembrosdirectorio = models.ManyToManyField(Empresario, related_name="propietario_miembrosdirectorio", verbose_name="Miembros Directorio", blank=True, help_text="Actualice con F5")
	utilidades = models.CharField("Utilidades -último año-", max_length=255, null=True, blank=True)
	infoutilidades = models.CharField("Información Utilidades", max_length=255, null=True, blank=True)
	fuenteutilidades = models.ForeignKey(Fuente, related_name="fuente_utilidades_propietario", verbose_name="Fuente", null=True, blank=True, max_length=255, on_delete=models.PROTECT)
	sectores = models.ManyToManyField(Sector, verbose_name="Sectores de Actividad Socio", blank=True, help_text="Actualice con F5")
	fuentepropietario = models.ForeignKey(Fuente, verbose_name="Fuente", null=True, blank=True, max_length=255, on_delete=models.PROTECT)

class PorcentajePropietario(models.Model):
	class Meta:
			verbose_name_plural = 'Porcentajes Socios'
	socioporcentaje = models.ForeignKey(Sociedad, verbose_name="Socio", related_name="socio_porcentajep", null=True, blank=True, on_delete=models.PROTECT)
	porcentajesocio = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	fechaporcentaje = models.DateField("Fecha", null=True, blank=True)
	fuenteporcentajesocio = models.ForeignKey(Fuente, verbose_name="Fuente", null=True, blank=True, on_delete=models.PROTECT)
	propietarioporcentaje = models.ForeignKey(Propietario, null=True, blank=True, on_delete=models.PROTECT)

class Escrito(models.Model):
	class Meta:
			verbose_name = 'Medio Escrito'
			verbose_name_plural = 'Medios Escritos'
	TIPO_MEDIO = (
		('Diario', 'Diario'),
		('Revista', 'Revista'),
		)
	tipo = models.CharField("Tipo", max_length=100, null=True, blank=True, choices=TIPO_MEDIO)
	medio = models.CharField("Nombre", max_length=255, unique=True)
	def __unicode__(self):
		return self.medio
	asociadoaescrito = models.ForeignKey('self', related_name="escrito_asociadoaescrito", verbose_name="Asociado a Medio Escrito", null=True, blank=True, on_delete=models.PROTECT)
	asociadoaradio = models.ForeignKey('Radio', related_name="escrito_asociadoaradio", verbose_name="Asociado a Radio", null=True, blank=True, on_delete=models.PROTECT)
	asociadoacanaltv = models.ForeignKey('CanalTV', related_name="escrito_asociadoacanaltv", verbose_name="Asociado a Canal de TV", null=True, blank=True, on_delete=models.PROTECT)
	asociadoamediodigital = models.ForeignKey('MedioDigital', related_name="escrito_asociadoamediodigital", verbose_name="Asociado a Medio Digital", null=True, blank=True, on_delete=models.PROTECT)
	genero = models.ForeignKey(GeneroEscrito, null=True, blank=True, on_delete=models.PROTECT)
	PAGADO_GRATUITO = (
		('Pagado', 'Pagado'),
		('Gratuito', 'Gratuito'),
		)
	pagado_gratuito = models.CharField("Pagado o Gratuito", max_length=100, null=True, blank=True, choices=PAGADO_GRATUITO)
	inicio = models.DateField("Fecha Fundación", null=True, blank=True)
	inicioyear = models.IntegerField(('Año Fundación'), choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True, blank=True)
	CIRCULACION = (
		('Nacional', 'Nacional'),
		('Regional', 'Regional'),
		('Comunal', 'Comunal'),
		)
	circulacion = models.CharField("Circulación", max_length=100, null=True, blank=True, choices=CIRCULACION)
	region = models.ManyToManyField(Region, verbose_name="Región", blank=True)
	comuna = models.ManyToManyField(Comuna, verbose_name="Comuna", blank=True, help_text="Actualice con F5 - Si el medio tiene cobertura regional, no es necesario ingresar las comunas.")
	ciudad = models.ManyToManyField(Ciudad, verbose_name="Ciudad", blank=True, help_text="Actualice con F5 - Si ingresa la(s) comuna(s) correspondientes, no es necesario señalar la(s) ciudad(es).")
	periodicidad = models.ForeignKey(Periodicidad, verbose_name="Periodicidad", null=True, blank=True, on_delete=models.PROTECT)
	lectoria = models.CharField("Índice de Lectoría", max_length=100, null=True, blank=True)
	infolectoria = models.CharField("Información Lectoría", max_length=255, blank=True)
	fuentelectoria = models.ForeignKey(Fuente, related_name="fuente_lectoria_escrito", verbose_name="Fuente Lectoría", null=True, blank=True, max_length=255, on_delete=models.PROTECT)
	tiraje = models.CharField("Tiraje", max_length=100, null=True, blank=True)
	infotiraje = models.CharField("Información Tiraje", max_length=255, null=True, blank=True)
	fuentetiraje = models.ForeignKey(Fuente, related_name="fuente_tiraje_escrito", verbose_name="Fuente Tiraje", null=True, blank=True, max_length=255, on_delete=models.PROTECT)
	direccion = models.CharField("Dirección", max_length=255, blank=True, help_text="Calle-Nº-Comuna-Ciudad")
	sitioweb = models.URLField("Sitio WEB", max_length=255, null=True, blank=True, help_text="http://...")
	propietario = models.ManyToManyField(Propietario, related_name="propietario_escrito", verbose_name="Empresa Controladora", max_length=255, blank=True, help_text="Actualice con F5")
	fuentepropiedad = models.ForeignKey(Fuente, related_name="fuente_propiedad_escrito", verbose_name="Fuente Propiedad", null=True, blank=True, max_length=255, on_delete=models.PROTECT)
	telefono = models.CharField("Teléfono", max_length=100, null=True, blank=True)
	observaciones = models.TextField("Observaciones", null=True, blank=True)
	anexos = models.TextField("Anexos", null=True, blank=True)
	check = models.BooleanField("Terminado", default=None)

class GeneroRadio(models.Model):
	class Meta:
			verbose_name = 'Género Radio'
			verbose_name_plural = 'Géneros Radios'
	genero = models.CharField("Género", max_length=255, unique=True)
	def __unicode__(self):
		return self.genero

class Radio(models.Model):
	class Meta:
			verbose_name = 'Radio'
			verbose_name_plural = 'Radios'
	medio = models.CharField("Nombre", max_length=255, unique=True)
	def __unicode__(self):
		return self.medio
	asociadoaescrito = models.ForeignKey('Escrito', related_name="radio_asociadoaescrito", verbose_name="Asociado a Medio Escrito", null=True, blank=True, on_delete=models.PROTECT)
	asociadoaradio = models.ForeignKey('self', related_name="radio_asociadoaradio", verbose_name="Asociado a Radio", null=True, blank=True, on_delete=models.PROTECT)
	asociadoacanaltv = models.ForeignKey('CanalTV', related_name="radio_asociadoacanaltv", verbose_name="Asociado a Canal de TV", null=True, blank=True, on_delete=models.PROTECT)
	asociadoamediodigital = models.ForeignKey('MedioDigital', related_name="radio_asociadoamediodigital", verbose_name="Asociado a Medio Digital", null=True, blank=True, on_delete=models.PROTECT)
	genero = models.ForeignKey(GeneroRadio, related_name="radio_genero", null=True, blank=True, on_delete=models.PROTECT)
	FRECUENCIA = (
		('AM', 'AM'),
		('FM', 'FM'),
		('AM y FM', 'AM y FM'),
		)
	frecuencia = models.CharField("Frecuencia", max_length=100, null=True, blank=True, choices=FRECUENCIA)
	inicio = models.DateField("Fecha Fundación", null=True, blank=True)
	inicioyear = models.IntegerField(('Año'), choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True, blank=True)
	indiceaudiencia = models.CharField("Índice de Audiencia", max_length=100, null=True, blank=True)
	infoaudiencia = models.CharField("Información de Índice Audiencia", max_length=255, blank=True)
	fuenteaudiencia = models.ForeignKey(Fuente, related_name="fuente_audiencia_radio", verbose_name="Fuente Audiencia", null=True, blank=True, max_length=255, on_delete=models.PROTECT)
	COBERTURA = (
		('Nacional', 'Nacional'),
		('Regional', 'Regional'),
		('Comunal', 'Comunal'),
		)
	cobertura = models.CharField("Cobertura", max_length=100, null=True, blank=True, choices=COBERTURA)
	region = models.ManyToManyField(Region, verbose_name="Región", related_name="radio_region", blank=True)
	comuna = models.ManyToManyField(Comuna, verbose_name="Comuna", blank=True, help_text="Actualice con F5 - Si el medio tiene cobertura regional, no es necesario ingresar las comunas.")
	ciudad = models.ManyToManyField(Ciudad, verbose_name="Ciudad", related_name="radio_ciudad", blank=True, help_text="Actualice con F5 - Si ingresa la(s) comuna(s) correspondientes, no es necesario señalar la(s) ciudad(es).")
	direccion = models.CharField("Dirección", max_length=255, blank=True, help_text="Calle-Nº-Comuna-Ciudad")
	sitioweb = models.URLField("Sitio WEB", max_length=255, null=True, blank=True, help_text="http://...")
	propietario = models.ManyToManyField(Propietario, related_name="propietario_radio", verbose_name="Empresa Controladora", max_length=255, blank=True, help_text="Actualice con F5")
	fuentepropiedad = models.ForeignKey(Fuente, related_name="fuente_propiedad_radio", verbose_name="Fuente Propiedad", null=True, blank=True, max_length=255, on_delete=models.PROTECT)
	telefono = models.CharField("Teléfono", max_length=100, null=True, blank=True)
	observaciones = models.TextField("Observaciones", null=True, blank=True)
	anexos = models.TextField("Anexos", null=True, blank=True)
	check = models.BooleanField("Terminado", default=None)

class GeneroCanalTV(models.Model):
	class Meta:
			verbose_name = 'Género Canal TV'
			verbose_name_plural = 'Géneros Canales TV'
	genero = models.CharField("Género", max_length=255, unique=True)
	def __unicode__(self):
		return self.genero

class CanalTV(models.Model):
	class Meta:
			verbose_name = 'Canal de TV'
			verbose_name_plural = 'Canales de TV'
	TIPO = (
		('Abierto', 'Abierto'),
		('Cable', 'Cable'),
		('Abierto y Cable', 'Abierto y Cable'),
		)
	tipo = models.CharField("Tipo", max_length=100, null=True, blank=True, choices=TIPO)
	medio = models.CharField("Nombre", max_length=255, unique=True)
	def __unicode__(self):
		return self.medio
	asociadoaescrito = models.ForeignKey('Escrito', related_name="canaltv_asociadoaescrito", verbose_name="Asociado a Medio Escrito", null=True, blank=True, on_delete=models.PROTECT)
	asociadoaradio = models.ForeignKey('Radio', related_name="canaltv_asociadoaradio", verbose_name="Asociado a Radio", null=True, blank=True, on_delete=models.PROTECT)
	asociadoacanaltv = models.ForeignKey('self', related_name="canaltv_asociadoacanaltv", verbose_name="Asociado a Canal de TV", null=True, blank=True, on_delete=models.PROTECT)
	asociadoamediodigital = models.ForeignKey('MedioDigital', related_name="canaltv_asociadoamediodigital", verbose_name="Asociado a Medio Digital", null=True, blank=True, on_delete=models.PROTECT)
	genero = models.ForeignKey(GeneroCanalTV, related_name="canaltv_genero", null=True, blank=True, on_delete=models.PROTECT)
	inicio = models.DateField("Fecha Fundación", null=True, blank=True)
	inicioyear = models.IntegerField(('Año'), choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True, blank=True)
	COBERTURA = (
		('Nacional', 'Nacional'),
		('Regional', 'Regional'),
		('Comunal', 'Comunal'),
		)
	cobertura = models.CharField("Cobertura", max_length=100, null=True, blank=True, choices=COBERTURA)
	rating = models.CharField("Rating", max_length=100, null=True, blank=True)
	inforating = models.CharField("Información de Rating", max_length=255, blank=True)
	fuenterating = models.ForeignKey(Fuente, related_name="fuente_rating_canaltv", verbose_name="Fuente Rating", null=True, blank=True, max_length=255, on_delete=models.PROTECT)
	region = models.ManyToManyField(Region, verbose_name="Región", related_name="canaltv_region", blank=True)
	comuna = models.ManyToManyField(Comuna, verbose_name="Comuna", blank=True, help_text="Actualice con F5 - Si el medio tiene cobertura regional, no es necesario ingresar las comunas.")
	ciudad = models.ManyToManyField(Ciudad, verbose_name="Ciudad", related_name="canaltv_ciudad", blank=True, help_text="Actualice con F5 - Si ingresa la(s) comuna(s) correspondientes, no es necesario señalar la(s) ciudad(es).")
	direccion = models.CharField("Dirección", max_length=255, blank=True, help_text="Calle-Nº-Comuna-Ciudad")
	sitioweb = models.URLField("Sitio WEB", max_length=255, null=True, blank=True, help_text="http://...")
	propietario = models.ManyToManyField(Propietario, related_name="propietario_canaltv", verbose_name="Empresa Controladora", max_length=255, blank=True, help_text="Actualice con F5")
	fuentepropiedad = models.ForeignKey(Fuente, related_name="fuente_propiedad_canaltv", verbose_name="Fuente Propiedad", null=True, blank=True, max_length=255, on_delete=models.PROTECT)
	telefono = models.CharField("Teléfono", max_length=100, null=True, blank=True)
	observaciones = models.TextField("Observaciones", null=True, blank=True)
	anexos = models.TextField("Anexos", null=True, blank=True)
	check = models.BooleanField("Terminado", default=None)

class GeneroMedioDigital(models.Model):
	class Meta:
			verbose_name = 'Género Medio Digital'
			verbose_name_plural = 'Géneros Medios Digitales'
	genero = models.CharField("Género", max_length=255, unique=True)
	def __unicode__(self):
		return self.genero

class MedioDigital(models.Model):
	class Meta:
			verbose_name = 'Medio Digital'
			verbose_name_plural = 'Medios Digitales'
	medio = models.CharField("Nombre", max_length=255, unique=True)
	def __unicode__(self):
		return self.medio
	sitioweb = models.URLField("Sitio WEB", max_length=255, null=True, blank=True, help_text="http://...")
	genero = models.ForeignKey(GeneroMedioDigital, related_name="mediodigital_genero", null=True, blank=True, on_delete=models.PROTECT)
	COBERTURA = (
		('Nacional', 'Nacional'),
		('Regional', 'Regional'),
		('Comunal', 'Comunal'),
		)
	cobertura = models.CharField("Cobertura", max_length=100, null=True, blank=True, choices=COBERTURA)
	CARACTERISTICA = (
		('Nativo', 'Nativo'),
		('Asociado', 'Asociado'),
		)
	nativoasociado = models.CharField("Nativo o Asociado", max_length=100, null=True, blank=True, choices=CARACTERISTICA)
	PAGADO_GRATUITO = (
		('Pagado', 'Pagado'),
		('Gratuito', 'Gratuito'),
		('Gratuito con Contenido Pagado', 'Gratuito con Contenido Pagado')
		)
	pagado_gratuito = models.CharField("Pagado o Gratuito", max_length=100, null=True, blank=True, choices=PAGADO_GRATUITO)
	asociadoaescrito = models.ForeignKey('Escrito', related_name="mediodigital_asociadoaescrito", verbose_name="Asociado a Medio Escrito", null=True, blank=True, on_delete=models.PROTECT)
	asociadoaradio = models.ForeignKey('Radio', related_name="mediodigital_asociadoaradio", verbose_name="Asociado a Radio", null=True, blank=True, on_delete=models.PROTECT)
	asociadoacanaltv = models.ForeignKey('CanalTV', related_name="mediodigital_asociadoacanaltv", verbose_name="Asociado a Canal de TV", null=True, blank=True, on_delete=models.PROTECT)
	asociadoamediodigital = models.ForeignKey('self', related_name="mediodigital_asociadoamediodigital", verbose_name="Asociado a Medio Digital", null=True, blank=True, on_delete=models.PROTECT)
	inicio = models.DateField("Fecha Fundación", null=True, blank=True)
	inicioyear = models.IntegerField(('Año'), choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True, blank=True)
	visitaspaginasvistas = models.IntegerField("Visitas Mes-Páginas Vistas", null=True, blank=True)
	visitasunicas = models.IntegerField("Visitas Mes-Visitas Únicas", null=True, blank=True)
	infovisitas = models.CharField("Información de Visitas", max_length=255, blank=True)
	fuentevisitas = models.ForeignKey(Fuente, related_name="fuente_visitas_mediodigital", verbose_name="Fuente", null=True, blank=True, max_length=255, on_delete=models.PROTECT)
	region = models.ManyToManyField(Region, verbose_name="Región", related_name="mediodigital_region", blank=True)
	comuna = models.ManyToManyField(Comuna, verbose_name="Comuna", blank=True, help_text="Actualice con F5 - Si el medio tiene cobertura regional, no es necesario ingresar las comunas.")
	ciudad = models.ManyToManyField(Ciudad, verbose_name="Ciudad", related_name="mediodigital_ciudad", blank=True, help_text="Actualice con F5 - Si ingresa la(s) comuna(s) correspondientes, no es necesario señalar la(s) ciudad(es).")
	direccion = models.CharField("Dirección", max_length=255, blank=True, help_text="Calle-Nº-Comuna-Ciudad")
	propietario = models.ManyToManyField(Propietario, related_name="propietario_mediodigital", verbose_name="Empresa Controladora", max_length=255, blank=True, help_text="Actualice con F5")
	fuentepropiedad = models.ForeignKey(Fuente, related_name="fuente_propiedad_mediodigital", verbose_name="Fuente Propiedad", null=True, blank=True, max_length=255, on_delete=models.PROTECT)
	telefono = models.CharField("Teléfono", max_length=100, null=True, blank=True)
	observaciones = models.TextField("Observaciones", null=True, blank=True)
	anexos = models.TextField("Anexos", null=True, blank=True)
	check = models.BooleanField("Terminado", default=None)

class Cargo(models.Model):
	class Meta:
			verbose_name = 'Cargo'
			verbose_name_plural = 'Cargos'
	cargo = models.CharField("Cargo", max_length=255, unique=True)
	def __unicode__(self):
		return self.cargo

class CargoEjecutivo(models.Model):
	class Meta:
			verbose_name = 'Cargo Ejectutivo'
			verbose_name_plural = 'Cargos Ejecutivos'
	ejecutivocargo = models.ForeignKey(Ejecutivo, verbose_name="Ejecutivo", related_name="ejecutivo_cargo", null=True, blank=True, on_delete=models.PROTECT)
	fechacargo = models.DateField("Fecha", null=True, blank=True)
	cargo = models.ForeignKey(Cargo, verbose_name="Cargo", related_name="cargo_ejecutivo", null=True, blank=True, on_delete=models.PROTECT)
	escrito = models.ForeignKey(Escrito, null=True, blank=True, on_delete=models.PROTECT)
	canaltv = models.ForeignKey(CanalTV, null=True, blank=True, on_delete=models.PROTECT)
	radio = models.ForeignKey(Radio, null=True, blank=True, on_delete=models.PROTECT)
	mediodigital = models.ForeignKey(MedioDigital, null=True, blank=True, on_delete=models.PROTECT)

class TipoDocumento(models.Model):
	class Meta:
			verbose_name = 'Tipo de Regulación'
			verbose_name_plural = 'Tipos de Regulación'
	tipodocumento = models.CharField("Tipo", max_length=255, unique=True)
	def __unicode__(self):
		return self.tipodocumento

class Regulacion(models.Model):
	class Meta:
			verbose_name = 'Regulación'
			verbose_name_plural = 'Regulaciones'
	documento = models.CharField("Documento", max_length=255, unique=True)
	tipodocumento = models.ForeignKey(TipoDocumento, verbose_name="Tipo de Regulación", null=True, blank=True, on_delete=models.PROTECT)
	descripciondocumento = models.TextField("Descripción", null=True, blank=True, help_text="Detalle del texto en relación a la industria de medios")
	actores = models.TextField("Entidades Involucradas", null=True, blank=True, help_text="Nombre de la entidad involucrada(gremio,ong,etc.)-Explicación de la situación(lobby,rrpp,vocería,etc.")
	linkdocumento = models.URLField("Link", null=True, blank=True, help_text="http://...")