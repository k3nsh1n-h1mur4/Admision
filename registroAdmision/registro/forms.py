from django import forms

from .models import Users, Worker, Candidate


class registerUsersForm(forms.Form):
	username = forms.CharField(required=True, widget=forms.TextInput(attrs={
											'class' : 'form-control'
								}))
	password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
											'class' : 'form-control'
								}))
	email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
											'class' : 'form-control'
								}))


class loginForm(forms.ModelForm):
	class Meta:
		model = Users
		exclude = ['email']


class registerWorkerForm(forms.ModelForm):
	class Meta:
		model = Worker
		fields = '__all__'


class updateWorkerForm(forms.ModelForm):
	class Meta:
		model = Worker
		fields = ['folio', 'nombre', 'categoria', 'matricula', 'uadscripcion', 'antiguedad', 'tipoC', 'domicilio', 'telefono', 'correo', 'rSocial', 'nPropuesta', 'observaciones']
		exclude = ('created_at', 'user_id')	





class registerCandidateForm(forms.ModelForm):
	class Meta:
		model = Candidate
		fields = '__all__'


class updateCandidateForm(forms.ModelForm):
	class Meta:
		model = Candidate
		fields = ['nombre', 'categoriaA', 'edad', 'zona', 'parentesco', 'domicilio', 'telefono', 'correo', 'rSocial']
		exclude = ( 'created_at', 'worker_id')
