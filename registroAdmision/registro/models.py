from django.db import models

# Create your models here.

class Users(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=150)
	email = models.EmailField(max_length=150)

	def __str__(self):
		return self.username



class Worker(models.Model):
	folio = models.CharField(max_length=800 ,unique=True, blank=False)
	nombre = models.CharField(max_length=100, unique=True, blank=True)
	categoria = models.CharField(max_length=100, unique=False, blank=True)
	matricula = models.CharField(max_length=100, unique=True, blank=True)
	uadscripcion = models.CharField(max_length=150, unique=False, blank=True)
	antiguedad = models.CharField(max_length=50, unique=False, blank=True)
	tipoC = models.CharField(max_length=50, unique=False, blank=True)
	domicilio = models.CharField(max_length=150, unique=False, blank=True)
	telefono = models.CharField(max_length=30, unique=False, blank=True)
	correo = models.CharField(max_length=100, unique=False, blank=True)
	rSocial = models.CharField(max_length=150, unique=False, blank=True)
	nPropuesta = models.CharField(max_length=20, unique=False, blank=True)
	observaciones = models.CharField(max_length=250, blank=True)
	created_at = models.DateField(auto_now_add=True)
	user_id = models.ForeignKey('Users', on_delete=models.CASCADE)

	def __str__(self):
		return self.matricula

		



class Candidate(models.Model):
	nombre = models.CharField(max_length=100, unique=True, blank=True)
	categoriaA = models.CharField(max_length=100, unique=False, blank=True)
	edad = models.CharField(max_length=20, unique=False, blank=True)
	zona = models.CharField(max_length=100, unique=False, blank=True)
	parentesco = models.CharField(max_length=100, unique=False, blank=True)
	domicilio = models.CharField(max_length=100, unique=False, blank=True)
	telefono = models.CharField(max_length=30, unique=False, blank=True)
	correo = models.EmailField(max_length=150)
	rSocial = models.CharField(max_length=150, unique=False, blank=True)
	created_at = models.DateField(auto_now_add=True)
	worker_id = models.ForeignKey('Worker', on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre
