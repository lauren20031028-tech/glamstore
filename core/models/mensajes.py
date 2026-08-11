from django.db import models

class MensajeContacto(models.Model):
    idMensaje = models.AutoField(primary_key=True, db_column='idMensaje')
    nombre = models.CharField(max_length=50, db_column='nombre')
    email = models.CharField(max_length=100, db_column='email')
    asunto = models.CharField(max_length=255, db_column='asunto')
    mensaje = models.TextField(db_column='mensaje')
    telefono = models.CharField(max_length=20, blank=True, null=True, db_column='telefono')
    fecha = models.DateTimeField(auto_now_add=True, db_column='fecha')
    leido = models.BooleanField(default=False, db_column='leido')

    class Meta:
        db_table = 'mensajes_contacto'
        managed = True
        app_label = 'core'
    
    def __str__(self):
        return f"{self.nombre} - {self.asunto}"