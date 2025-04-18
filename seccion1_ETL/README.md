# Guía de Instalación y Ejecución del Pipeline ETL
## Requisitos Previos
- Python 3.8 o superior
- Docker y Docker Compose
- Git (opcional, para clonar el repositorio)
## Pasos de Instalación
### 1. Configuración del Entorno Virtual

```bash
# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual (Windows)
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```
### 2. Configuración Manual (Sin Docker)

```bash
# Configurar variables de entorno para la conexión a PostgreSQL
set DB_HOST=localhost
set DB_PORT=5432
set DB_USER=usuario
set DB_PASSWORD=contraseña
set DB_NAME=etl_db

# Ejecutar el pipeline
python run_pipeline.py
```

### 3. Configuración con Docker
```bash
# Construir las imágenes de Docker
docker-compose build

# Iniciar los servicios
docker-compose up -d

# Ver los logs
docker-compose logs -f
```

## Verificación de la Instalación

Para verificar que todo está funcionando correctamente:

1. Revisa los logs de Docker para asegurarte de que no hay errores:

```bash
docker-compose logs -f
```

2. Conéctate a la base de datos para verificar que las tablas y la vista se han creado:

```bash
docker exec -it seccion1_etl_db_1 psql -U user -d etl_db
```

3. En la consola de PostgreSQL, ejecuta:

```bash
\dt
\dv
SELECT * FROM daily_company_transactions LIMIT 10;
```

## Solución de Problemas
Si encuentras errores durante la ejecución:

1. Verifica que la base de datos esté accesible
2. Asegúrate de que el archivo CSV esté en la ubicación correcta
3. Revisa los logs para identificar errores específicos