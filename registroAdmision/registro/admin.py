from django.contrib import admin

from .models import Users, Worker, Candidate
# Register your models here.


class candidateStackedInline(admin.StackedInline):
    model = Candidate


class workerModelAdmin(admin.ModelAdmin):
    search_fields = ('folio', 'matricula', 'nombre')
    list_display = ('id', 'folio', 'matricula', 'nombre') 
    inlines = [candidateStackedInline]

class candidateModelAdmin(admin.ModelAdmin):
    search_fields = [('nombre'),]
    #model = Candidate
    list_display = ('nombre', 'worker_id_id', 'parentesco',)



admin.site.register(Users)
admin.site.register(Worker, workerModelAdmin)
admin.site.register(Candidate, candidateModelAdmin)
