from django.contrib import admin
from .models import Project

# Register your models here.

#configuracion extendida al administrador
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

admin.site.register(Project, ProjectAdmin)


