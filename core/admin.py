from django.contrib import admin
from core.models import usuario


class usuarioAdmin(admin.ModelAdmin):
    #imagen (imagen_tag  )
    fields = ( 'image_tag','rut','nombre','apaterno','amateno','telefono','fech_nac', 'email_user','foto',)
    readonly_fields = ('image_tag',)
    list_display = ('image_tag', 'rut', 'NombreCompleto','telefono','fech_nac', 'email_user')
    #imagen
    search_fields = ['rut', 'nombre', 'apaterno']

admin.site.register(usuario, usuarioAdmin)