# 🔍 Missing Number App

Aplicación en Python con interfaz web que permite extraer un número de un conjunto de los primeros 100 números naturales y luego calcular cuál fue el número extraído.

## Cómo Ejecutar la Aplicación

1. Clona el repositorio o descarga los archivos.

2. Instala Flask (si aún no lo tienes):

   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el servidor:
   ```bash
   python main.py
   ```
4. Abre tu navegador en:
    ```bash
    (http://localhost:5000)
   ```

## Descripción del Problema
Calcular el número faltante de un conjunto de los primeros 100 números naturales del cual se extrajo uno.

Requisitos cumplidos:
- ✅ Clase que representa el conjunto.
- ✅ Método para extraer un número.
- ✅ Método para identificar el número faltante.
- ✅ Validación de entrada (número entre 1 y 100).
- ✅ Interfaz gráfica con HTML, dinamismo con JS y estilos CSS.
- ✅ API REST adicional para integración externa.

## Interfaz Web

Formulario en HTML con estilos modernos que permite al usuario ingresar un número para extraer. Al enviar el formulario, se muestra cuál fue el número extraído.

## API REST

También puedes interactuar con la aplicación mediante la API:

POST ``` /api/extract ```
**Request:**
``` 
{
  "number": 42
}
```
**Response (200 OK):**
``` 
{
  "extracted": 42,
  "all_extracted": [1, 42]
}
```
**Errores (400 Bad Request):**
``` 
{
   "error": "El número debe estar entre 1 y 100."
}
```

## Validaciones
- Solo se aceptan números enteros entre 1 y 100.
- El número no debe haber sido extraído anteriormente.
- El conjunto se reinicia automáticamente si ya se extrajo un número antes.
- Se van tachando los numeros del conjunto de números

## Snapshots

-  Interfaz principal
![Interfaz](/snapshots/interfaz.png)

-  Uso de la interfaz
![Extraccion](/snapshots/extraccion.png)

-  Manejo de erorres
![Errores](/snapshots/errores.png)