from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
	path('users/register', views.registerUsers, name='registro'),
	path('users/login', views.login_view, name='login_view'),
	path('users/logout', views.logout_view, name='logout_view'),
	path('worker/register', views.registerWorker, name='registroWorker'),
	path('worker/list', views.listWorkers, name='listWorkers'),
	path('worker/edit/<int:id>', views.updateWorkers, name='updateWorkers'),
	path('worker/delete/<int:id>', views.deleteWorker, name='deleteWorker'),
	path('candidates/register/<int:id>', views.registerCandidate, name='registroCandidate'),
	path('candidates/list', views.listC, name='listC'),
	path('candidate/delete/<int:id>', views.deleteCandidate, name='deleteCandidate'),
	path('candidates/edit/<int:id>', views.updateCandidate, name='updateCandidate'),
    path('pdfWorkers/', views.exportPdf, name='exportPdf'),
    path('pdfCandidates/', views.exportPdfC, name='exportPdfC'),
	path('worker/export_csv_worker/', views.export_csv_worker, name='export_csv_worker'),
	path('candidates/export_csv_candidates', views.export_csv_candidates, name='export_csv_candidates'),

]
