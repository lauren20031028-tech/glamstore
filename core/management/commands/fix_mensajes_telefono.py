from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Agrega la columna telefono a la tabla mensajes_contacto si no existe'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            try:
                # Verificar si la columna ya existe
                cursor.execute("""
                    SELECT COLUMN_NAME 
                    FROM INFORMATION_SCHEMA.COLUMNS 
                    WHERE TABLE_NAME = 'mensajes_contacto' 
                    AND COLUMN_NAME = 'telefono'
                """)
                
                if cursor.fetchone():
                    self.stdout.write(
                        self.style.SUCCESS('✓ La columna telefono ya existe en mensajes_contacto')
                    )
                else:
                    # Agregar la columna
                    cursor.execute("""
                        ALTER TABLE mensajes_contacto 
                        ADD COLUMN telefono VARCHAR(20) NULL DEFAULT NULL
                    """)
                    self.stdout.write(
                        self.style.SUCCESS('✓ Columna telefono agregada correctamente a mensajes_contacto')
                    )
                    self.stdout.write(
                        self.style.WARNING('⚠ Por favor, ahora descomentar el campo telefono en core/models/mensajes.py')
                    )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'✗ Error: {str(e)}')
                )

