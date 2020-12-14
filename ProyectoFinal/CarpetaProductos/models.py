from django.db import models
from django.contrib import admin

class empleado(models.Model):
    usuarios  = models.CharField(max_length=30)
    Contrasenia = models.CharField(max_length=30)
    Roles = models.CharField(max_length=30)

    def __str__(self):
        return self.usuarios
