## 📖 Documentación de Gestión y Pruebas

### 1. Carga Inicial con `seed_info.py`

Este script automatiza la población de la base de datos sin necesidad de ingresar registros manualmente uno por uno.

* **Funcionamiento:** Utiliza el entorno de ejecución de Django (`django.setup()`) para acceder a los modelos. Primero limpia las tablas (para evitar duplicados) y luego crea 5 autores y 10 libros relacionados aleatoriamente.
* **Uso:** Se ejecuta desde la terminal del sistema (fuera de la shell de Python).
* **Comando:**
```bash
python seed_info.py

```



### 2. Carga Masiva vía Django Shell

Ideal para realizar pruebas rápidas de volumen o manipular datos en tiempo real mediante código Python.

* **Funcionamiento:** Abre una instancia interactiva que carga toda la configuración de tu proyecto Django.
* **Uso:** 1. Iniciar la shell: `python manage.py shell`.
2. Importar los modelos necesarios.
3. Ejecutar bucles `for` para crear registros en masa utilizando el ORM de Django.
* **Beneficio:** Permite probar la lógica de los modelos y las relaciones (One-to-Many) de forma inmediata.

### 3. Pruebas de Endpoints con `cURL`

`cURL` es una herramienta de línea de comandos para transferir datos con sintaxis de URL. Es la forma más pura de probar una API sin interfaz gráfica.

* **Estructura del comando:**
* `-X GET`: Define el método HTTP.
* `-H "Content-Type: application/json"`: Indica que esperamos/enviamos datos en formato JSON.


* **Ventaja:** Permite verificar que el servidor está escuchando y que las rutas en `urls.py` apuntan correctamente a las funciones en `views.py`.

### 4. Automatización con Postman (OpenAPI/YAML)

Postman permite organizar las peticiones en colecciones y realizar pruebas más complejas.

* **El archivo YAML:** Utilizamos el estándar **OpenAPI 3.0**. Este archivo describe la "forma" de tu API: qué rutas existen, qué parámetros reciben (como el `id` del libro) y qué códigos de respuesta (`200 OK`, `404 Not Found`) se esperan.
* **Flujo de trabajo:**
1. **Importar:** Se carga el archivo `.yml` en Postman.
2. **Colección:** Postman genera automáticamente una carpeta con todas las peticiones listas para hacer clic en **Send**.
3. **Documentación:** El mismo archivo sirve como documentación viva para otros desarrolladores.



---

### Resumen de Comandos Rápidos

| Tarea | Herramienta | Comando / Acción |
| --- | --- | --- |
| **Poblar DB** | Script Python | `python seed_info.py` |
| **Pruebas ORM** | Django Shell | `python manage.py shell` |
| **Test Manual** | cURL | `curl -X GET http://127.0.0.1:8000/libros/` |
| **Test Visual** | Postman | Importar `libreria_openapi.yml` |
