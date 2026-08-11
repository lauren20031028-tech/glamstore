from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_create_all_base_tables'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS imagenes_productos (
                id BIGINT AUTO_INCREMENT PRIMARY KEY,
                id_producto BIGINT NOT NULL,
                nombre_archivo VARCHAR(255) NOT NULL,
                ruta VARCHAR(255) NOT NULL,
                contenido LONGBLOB NOT NULL,
                fecha_subida TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS imagenes_productos;"
        ),
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS imagenes_categorias (
                id BIGINT AUTO_INCREMENT PRIMARY KEY,
                id_categoria INTEGER NOT NULL,
                nombre_archivo VARCHAR(255) NOT NULL,
                ruta VARCHAR(255) NOT NULL,
                contenido LONGBLOB NOT NULL,
                fecha_subida TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS imagenes_categorias;"
        ),
    ]
