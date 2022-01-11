from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.core.paginator import Paginator

from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

from django.contrib.auth.decorators import login_required


from django.contrib import messages

from django.template import Context

from django.contrib.auth.models import User

from .forms import registerUsersForm, registerWorkerForm, registerCandidateForm, loginForm, updateWorkerForm, updateCandidateForm
from .models import Users, Worker, Candidate

import django_excel as excel

import csv

# Create your views here.


def index(request):
	return render(request, 'index.html')


def registerUsers(request):
	form = registerUsersForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		email = form.cleaned_data.get('email')
		print(username)
		print(password)
		print(email)

		user = User.objects.create_user(username, password, email)
		if user:
			login(request, user)
			return redirect('registroWorker')
	return render(request, 'users/register.html', {'form':form})


def login_view(request):
	print(request.user.is_authenticated)
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		print(username)
		print(password)
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			print(user.id)
			messages.success(request, 'Bienvenido {}'.format(user.username))
			return redirect('registroWorker')
			#return render(request, 'users/auth.html', {'form':form})
		else:
			messages.error(request, 'Usuario o contraseña no válidos')
			return redirect('login_view')

	return render(request, 'users/auth.html')


def logout_view(request):
	logout(request)
	messages.success(request, 'Usuario deslogueado')
	return redirect('login_view')



@login_required(login_url='/admision/users/login')
def registerWorker(request):
	form = registerWorkerForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			try:
				form.save()
				return redirect('listWorkers')
			except:
				pass

		else:
			form = registerWorkerForm()
	return render(request, 'worker/register.html', {'form':form})


@login_required(login_url='/admision/users/login')
def listWorkers(request):
	ctx = Worker.objects.all()
	#paginator = Paginator(ctx, 15)
	#page_number = request.GET.get('page')
	#page_obj = paginator.get_page(page_number)
	if ctx:
		print('Hay datos')
	else:
		pass
	return render(request, 'worker/list.html', {'ctx':ctx})


@login_required(login_url='/admision/users/login')
def updateWorkers(request, id):
	id = Worker.objects.get(id=id)
	print(id)
	if request.method == 'GET':
		form = updateWorkerForm(instance=id)
	else:
		form = updateWorkerForm(request.POST, instance=id)
		print(form)
		#context = {'id':id}, {'form': form}
		if form.is_valid():#request.method == 'POST' and form.is_valid():
			try:
				#matricula = request.POST.cleaned_data('matricula')
				form.save()
				return redirect('listWorkers')
			except:
				pass
		else:
			form = updateWorkerForm()	
	return render(request, 'worker/edit.html', {'id':id, 'form':form})

		
@login_required(login_url='/admision/users/login')
def deleteWorker(request, id):
	context = Worker.objects.get(id=id)
	print(context)
	if context:
		context.delete()
		return redirect('listWorkers')
	return render(request, 'worker/list.html', {'context':context})


@login_required(login_url='/admision/users/login')
def registerCandidate(request, id):
	context = Worker.objects.get(id=id)
	print(context)
	form = registerCandidateForm(request.POST)
	if request.method == 'POST' and form.is_valid():
		try:
			form.save()
			return redirect('')
		except:
			pass
	return render(request, 'candidates/register.html', {'context' : context, 'form' : form})



def listC(request):
	resp = Candidate.objects.all()
	print(resp)
	return render(request, 'candidates/lists.html', {'resp':resp})


def deleteCandidate(request, id):
	context = Candidate.objects.get(id=id)
	if context:
		context.delete()
		return redirect('listC')
	return render(request, 'candidates/lists.html', {'context':context})
	


@login_required(login_url='/admision/users/login')
def updateCandidate(request, id):
	id = Candidate.objects.get(id=id)
	if request.method == 'GET':
		form = updateCandidateForm(instance=id)
	else:
		form = updateCandidateForm(request.POST, instance=id)
		print(form)
		if form.is_valid():
			try:
				form.save()
				return redirect('')
			except:
				pass
		else:
			form = updateCandidateForm()
	return render(request, 'candidates/edit.html', {'id':id, 'form':form})



def search(request, matricula):
	matricula = Worker.objects.get('matricula')
	print(matricula)


def exportPdf(request):
    if request.method == 'GET':
        export = []
        export.append([
            'Folio',
            'Nombre',
            'Categoria',
            'Matricula',
            'Unidad Adscripcion',
            'Antiguedad',
            'T. Contratacion',
            'Domicilio',
            'Telefono',
            'Correo',
            'Red Social',
            '# Propuesta',
        ])
        results = Worker.objects.all()
        for result in results:
            export.append([
                result.folio,
                result.nombre,
                result.categoria,
                result.matricula,
                result.uadscripcion,
                result.antiguedad,
                result.tipoC,
                result.domicilio,
                result.telefono,
                result.correo,
                result.rSocial,
                result.nPropuesta,
            ])
    sheet = excel.pe.Sheet(export)
    return excel.make_response(sheet, file_type="xlsx", file_name="Trabajadores")


def exportPdfC(request):
    if request.method == 'GET':
        export = []
        export.append([
            'Nombre',
            'Categoria',
            'Edad',
            'Parentesco',
            'Domicilio',
            'Telefono',
            'Correo',
            'Red Social',
            'Zona',
        ])
        results = Candidate.objects.all()
        for result in results:
            export.append([
                result.nombre,
                result.categoriaA,
                result.edad,
                result.parentesco,
                result.domicilio,
                result.telefono,
                result.correo,
                result.rSocial,
                result.zona,
            ])
    sheet = excel.pe.Sheet(export)
    return excel.make_response(sheet, file_type="xlsx", file_name="Candidatos")





def export_csv_worker(request):
    data = Worker.objects.all()
    response = HttpResponse(data, headers={
        'Content-Type': 'text/csv',
        'Content-Disposition': 'attachment; filename="encuestaSituacional.csv"',
    })

    writer = csv.writer(response)
    writer.writerow(['id', 'folio', 'nombre', 'categoria', 'matricula', 'uadscripcion', 'antiguedad', 'tipoC', 'domicilio', 'telefono', 'correo', 'rSocial', 'nPropuesta'])

    for datas in data:
        writer.writerow([datas.id, datas.folio, datas.nombre, datas.categoria, datas.matricula, datas.uadscripcion, datas.antiguedad, datas.tipoC, datas.domicilio, datas.telefono, datas.correo, datas.rSocial, datas.nPropuesta])

    return response



def export_csv_candidates(request):
    data = Candidate.objects.all()
	#data1 = Worker.objects.all()
    response = HttpResponse(data, headers={
        'Content-Type': 'text/csv',
        'Content-Disposition': 'attachment; filename="registroCandidatos.csv"',
    })

    writer = csv.writer(response)
    writer.writerow(['id', 'nombre', 'categoriaA', 'edad', 'parentesco', 'domicilio', 'telefono', 'correo', 'rSocial', 'zona'])

    for datas in data:
        writer.writerow([datas.id, datas.nombre, datas.categoriaA, datas.edad, datas.parentesco, datas.domicilio, datas.telefono, datas.correo, datas.rSocial, datas.zona, datas.worker_id])

    return response