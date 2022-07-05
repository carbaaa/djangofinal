from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfiles(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='perfiles')
    telefono = models.CharField(max_length=13,blank=True)
    tipo = models.CharField(max_length=15,blank=True)
    imagen = models.ImageField(upload_to='imagenes', blank=True)
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'