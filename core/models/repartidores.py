from django.db import models

class Repartidor(models.Model):
    idRepartidor = models.AutoField(primary_key=True, db_column='idRepartidor')
    nombreRepartidor = models.CharField(max_length=50, null=True, db_column='nombreRepartidor')
    telefono = models.CharField(max_length=20, null=True, db_column='telefono')
    email = models.EmailField(max_length=100, null=True, blank=True, db_column='email')
    estado_turno = models.CharField(max_length=20, null=True, blank=True, db_column='estado_turno')

    class Meta:
        db_table = 'repartidores'   
        managed = False             
        app_label = 'core'
    
    def __str__(self):
        return self.nombreRepartidor or f"Repartidor {self.idRepartidor}"
