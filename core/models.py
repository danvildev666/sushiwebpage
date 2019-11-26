import os
from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe


class usuario (models.Model):
    rut = models.CharField(max_length=10)
    nombre =models.CharField(max_length=30)
    apaterno = models.CharField(max_length=30)
    amateno = models.CharField(max_length=30)
    telefono = models.PositiveSmallIntegerField()
    fech_nac = models.DateField()
    email_user =models.EmailField()
    foto = models.ImageField(upload_to='Photos', null=True, blank=True)

    def NombreCompleto (self):
        Cadenanombre = "{0} {1}"
        return  Cadenanombre.format(self.nombre, self.apaterno)

    def __str__(self):
        return self.NombreCompleto()

    def image_tag(self):
        return mark_safe('<img src="/Photos/%s" width="100" height="100" />' % (self.foto))
       

    class Meta:
        verbose_name ="Usuario"  
        verbose_name_plural ="usuarios" 

    

