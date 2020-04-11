# Checklist Sobre el Diseño en Capas

El siguiente checklist permite una fácil detección de malas prácticas y posibles correcciones para implementar el patrón de diseño en capas.

## Checklist

### General

- [ ] El sistema debe estar **DESPLEGADO**
    - [ ] Debe estar online y accesible desde cualquier dispositivo, es decir no desde localhost (Sólo para Web)
    - [ ] En caso de no ser Web, debe poder installarse desde PyPi usando pip install
- [ ] Cada capa debe seguir las buenas prácticas de formato
    - [ ] En caso de ser un único archivo el archivo deberá tener el nombre de la capa (db.py, controller.py, presentation.py)
    - [ ] En caso de tener varios archivos para una misma capa, deben estar todos dentro de una carpeta con el nombre correspondiente
    - [ ] Cualquiera sea el caso, debe haber un archivo app.py en la raiz que será el que deberá ejecutar la aplicación.

### Presentación (Flask, Django, Kivy, etc.)

- [ ] **NO** se utiliza ninguna función, objeto o clase de la capa de Datos.
- [ ] Toda la lógica de los elementos interactivos (botones, menúes, etc.) se ejecuta mediante una función en la capa de negocio y **NO** dentro de elementos de interfaz.
- [ ] Esta capa funciona aunque se modifique cualquier archivo de la capa de datos.
- [ ] Debe cumplir con los estándares de formato:
    - Si es un único archivo, debe llamarse **views.py**
    - Si son múltiples archivos, deben estar todos en una carpeta **views**

### Negocio

- [ ] Ninguna función realiza llamadas a la base de datos directamente ni con ORM, todas deben llamar a una función de la capa de datos.
- [ ] Ninguna función involucra elementos específicos de interfaz (Botones, HTML, etc.).
- [ ] Esta capa seguiría funcionando si se cambiara el motor de base de datos.
- [ ] Todas las funciones devuelven objetos de Negocio (Usuario, Reserva, Turno, etc.).
- [ ] Se debe validar al menos una regla de negocio
- [ ] Debe cumplir con los estándares de formato:
    - Si es un único archivo, debe llamarse **controller.py**
    - Si son múltiples archivos, deben estar todos en una carpeta **business** o **controller**

### Datos

- [ ] Todas las funciones devuelven objetos de Negocio (Usuario, Reserva, Turno, etc.).
- [ ] Todas las consultas a la base de datos se hacen desde esta capa.
- [ ] Solo se acceden a las funciones de esta capa desde la Capa de Negocio
- [ ] Se utiliza una base de datos (MySQL, Mongo, SQLite)
- [ ] Se encuentra disponible el Modelo de Dominio / Diagrama Entidad Relación (Usar https://draw.io/) o similar
- [ ] Debe cumplir con los estándares de formato:
    - Si es un único archivo, debe llamarse **db.py**
    - Si son múltiples archivos, deben estar todos en una carpeta **datos**
