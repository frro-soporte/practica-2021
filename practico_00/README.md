# Trabajo Práctico 0: Uso de Git y Github

Este trabajo práctico tiene como objetivo que el alumno se familiarice con el concepto de sistema de control de versiones (VCS) y en particular que aprenda a utilizar Git. Para ello se utilizará la plataforma online GitHub, que provee un entorno gratuito para hospedar los repositorios remotos, realizar Pull Requests y facilitar la tarea de control y corrección de errores.

Se recomienda que el alumno lea la siguiente [guia introductoria](https://elc.github.io/posts/git-guide-with-visual-interface/es/) creada por el alumno Ezequiel L. Castaño y que luego realice los ejercicios propuestos.

**NOTA**: Para esta actividad los alumnos deberán formar grupos de 2 personas. Estos grupos serán los definitivos por lo que se alienta la cooperación, cada integrante tendrá un rol diferente que determinará su tareas en las actividades.

El trabajo práctico consta de actividades grupales e individuales. Las actividades individuales tendrán el código **I** y las grupales el código **G**.

Cada grupo deberá asignar los siguientes roles a sus integrantes, los roles no pueden repetirse ni cambiarse luego de establecerse y cada integrante deberá tener un único rol:

1. Integrante `Rojo`
1. Integrante `Amarillo`

A partir de este momento las actividades grupales estarán enunciadas en función de los roles propuestos. Las actividades individuales deberán ser realizadas por cada integrante. Se llamará a cada integrante por el color de su rol.

## Restricciones importantes

Todo el trabajo deberá realizarse utilizando git, se podrá utilizar la consola o alguna aplicativo con interfaz gráfica pero **NO** se podrá utilizar el editor online de GitHub. Copiar y pegar el código en el editor online implica que el trabajo no está aprobado ya que no se están utilizando los conceptos esperados.

Los commits deben ser referidos a un tema, NO se aprobarán trabajos que realicen varios commits para un mismo tema, deberán modificarse los archivos y subirse en un único commit. Realizar varios commits por un mismo tema o un commit por archivo es una mala práctica e implica que no se están utilizando los conceptos esperados.

Cada usuario deberá utilizar su cuenta personal de GitHub durante todo el proceso, no se permiten cuentas comunitarias o grupales.

## Actividades

Se realizarán 3 actividades donde se explorarán los conceptos básicos de Git y GitHub. Se recomienda que cada actividad de realice durante el periodo de clases y que estén presentes todos los miembros del equipo. Se dispondrán de 2 clases de práctica para llevar a cabo este TP.

### Actividad 1: Inicialización con Git y GitHub

- **I1**: Crear una cuenta en GitHub - Nota: NO se admiten cuentas grupales, cada alumno deberá tener una cuenta independiente de GitHub, esto será fundamental para la corrección y aprobación.
- **I2**: Crear un repositorio que se llame "mi-primer-repositorio", utilizar la opción "Inicializar con un `README.md`" y agregar al usuario del docente como colaborador - Nota: Es importante que para evitar problemas futuros, los nombres de todos los repositorios y carpetas se escriban siempre en minúsculas y con guiones en lugar de espacios.
- **I3**: Clonar el repositorio creado al equipo local.
- **I4**: Modificar el archivo y realizar un commit: se debe borrar los contenidos del archivo `README.md` y reemplazarlos con los datos del alumno: Nombre, Apellido y Legajo. Luego se deberá realizar un commit con el título de "Modificar `README.md`"
- **I5**: Subir los cambios mediante un push: se debe realizar un push para que los cambios impacten en el repositorio remoto.
- **I6**: Crear un nuevo branch llamado 'agregar-encuesta' - Nota: la nomenglatura de los branches será la misma que la de los repositorios, todo en minúscula separada con guiones medios.
- **I7**: Cambiar al branch creado y agregar un archivo con nombre "encuesta.md" - En ese archivo el alumno deberá responder la siguiente pregunta: "¿Qué expectativa tiene de la materia?"
- **I8**: Realizar un commit y un push.
- **I9**: Realizar un Pull Request desde el branch 'agregar-encuesta' al 'master' del repositorio y agregar al usuario del docente como revisor. Con este paso se terminan las actividades de esta sección y docente realizará la corrección en función de lo hecho. En caso de haber cometido un error el alumno deberá solucionarlo, los cambios quedan reflejados automáticamente en la Pull Request, si se detectan errores, el docente lo comentará y le pedirá la revisión mediante la plataforma de GitHub.

### Actividad 2: Primer Trabajo Grupal

Las siguientes actividades serán grupales

- **G1**: `Rojo` deberá crear un repositorio con el nombre 'mi-primer-repositorio-en-equipo'. Deberá inicializar con un `README.md`.
- **G2**: `Rojo` deberá invitar a `Amarillo` y al usuario del docente como colaboradores.
- **G3**: Los dos integrantes deberán clonar el repositorio.
- **G4**: `Amarillo` modificará el `README.md` agregando el título "Trabajo en equipo" y en una nueva línea agregará su nombre y apellido.
- **G5**: `Amarillo` hará un commit y un push.
- **G6**: `Rojo` modificará el `README.md` y pondrá el título "Trabajo colaborativo" y en una nueva línea agregará su nombre y apellido.
- **G7**: `Rojo` hará commit y push, en este momento deberán surgir conflictos, `Rojo` deberá solucionarlos, realizar un nuevo commit y hacer push.
- **G8**: `Amarillo` hará pull y creará un nuevo branch con el nombre 'prueba-de-formatos'.
- **G9**: `Amarillo` deberá generar varios archivos de texto con distinto formato, cada uno con el contenido "Esto es una prueba". Los formatos a utilizar serán: .doc, .docx, .txt, .md, .pdf, .rtf - Nota: Puede requerirse distintos softwares para guardar en cada formato.
- **G10**: `Amarillo` deberá hacer un commit con el nombre 'agregar-archivos-basicos' y hacer un push.
- **G11**: `Rojo` deberá hacer un pull de ambos branches.
- **G12**: Todos los integrantes deberán entrar al repositorio desde github y verificar cuales de los formatos puede visualizarse correctamente y cuales no.
- **G13**: `Rojo` deberá agregar una imagen libre de derechos de autor a cada uno de los archivos (siempre que sea posible), hacer un commit y hacer un push.
- **G14**: `Amarillo` deberá verificar que la imagen pueda verse en GitHub y realizará un Pull Request a master y pondrá a `Rojo` y al docente como revisores.
- **G15**: `Rojo` verá la revisión y deberá solicitar desde la plataforma de Pull Request que se quiten los archivos que no pueden verse adecuadamente.
- **G16**: `Rojo` solicitará en la PR que `Amarillo` haga los cambios.
- **G17**: `Amarillo` realiza un pull, hace los cambios, realiza un commit, hace un push y notifica a `Rojo` desde la plataforma de los Pull Request con una mención (@) que los cambios necesarios fueron hechos.
- **G18**: `Rojo` verifica que todo se pueda visualizar correctamente online y escribe una mención (@) en la plataforma del Pull Request hacia el docente para que haga la corrección de la actividad. En la descripción de este Pull Request se deberá aclarar que rol tenía cada usuario

### Actividad 3: Mi primer sitio web con GitHub Pages

Las siguientes actividades serán una combinación de actividades grupales e individuales.

- **I1**: Cada integrante deberá crear un repositorio (inicializado con un `README.md`) con nombre '{nombre de usuario}.github.io' donde se reemplazará '`{nombre de usuario}`' con el nombre de cada uno de los usuarios. Además se deberá agregar a los demás integrantes y al docente como colaboradores.
- **I2**: Cada integrante deberá ir a la configuración del repositorio y habilitar las "GitHub Pages" en caso de que no estén habilitadas.
- **I3**: Cada integrante deberá hacer un clone de su propio repositorio y agregar un archivo index.html, realizar un commit y hacer push. El contenido del archivo deberá ser la estructura básica de HTML (html, head y body) sin formato, sin CSS ni Javascript. Deberá contener una etiqueta H1 con el nombre y apellido del integrante.
- **I4**: Cada integrante verificará que el sitio http://{nombre de usuario}.github.io está online y tiene el contenido esperado. También deberán verificar el sitios de los demás integrantes.
- **G5**: `Rojo` deberá crear un "Issue" en el repositorio de `Amarillo` con título "Falta Estilo - Agregar un color de fondo a la letra".
- **G6**: `Amarillo` deberá crear un "Issue" en el repositorio de `Rojo` con título "Faltan Imágenes - Agregar una imagen debajo del título".
- **G7**: Cada uno de los integrantes deberá realizar los cambios pertinentes en sus propios repositorios según el issue que creó el otro integrante y al realizar un commit el mensaje deberá finalizar con " - Closes #{numero del issue}" donde se deberá reemplazar {numero del issue} con el códgio (número luego del #) que GitHub asignó al issue creado.
- **G8**: `Amarillo` deberá crear un "Issue" en el repositorio de `Rojo` con título "Falta Estilo - Agregar un color de fondo a la letra".
- **G9**: `Rojo` deberá crear un "Issue" en el repositorio de `Amarillo` con título "Faltan Enlaces - Agregar enlace a los sitios de `Rojo`.
- **G10**: `Amarillo` deberá hacer un fork del repositorio de `Rojo`, crear un branch con un título similar al issue, resolver el problema, realizar un commit y crear una Pull Request al master de `Rojo` (**no al master del fork que se creó**).
- **G11**: `Rojo` deberá hacer un fork del repositorio de `Amarillo`, crear un branch con un título similar al issue, resolver el problema, realizar un commit y crear una Pull Request al master de `Amarillo` (**no al master del fork que se creó**).
- **G12**: Cada integrante deberá revisar el Pull Request y aprobarlo.
- **I13**: Cada integrante deberá crear un branch con el nombre 'detalles-finales' y realizar los cambios necesarios para que su sitio tenga las mismas caracteristicas que el de sus compañeros. Cada sitio deberá tener el estilo, la imagen y los enlaces. Luego se hará un commit, un push y se deberá realizar un Pull Request donde se lo asigne al docente como revisor, en este último paso se hará la evaluación. En la descripción de este Pull Request se deberá aclarar que rol tenía cada usuario

Luego de que la actividad quede aprobada, cada alumno tendrá la libertad de utilizar este último repositorio como desee, es una manera gratuita de alojar sitios web estáticos.

## Preparativos para los próximos Trabajos Prácticos

Luego de tener las 3 actividades aprobadas, se debe realizar un único Fork por equipo del repositorio de Práctica (donde estarán los próximos TPs). En ese repositorio se deben agregar a todos los integrantes como colaboradores y al docente. Cada integrante deberá utilizar su cuenta para trabajar ya que en el proceso de evaluación se tendrá en cuenta la participación individual.

El esquema de trabajo será el siguiente:

1. Cada equipo realiza el trabajo práctico en el repositorio grupal
1. El equipo al finalizar un trabajo práctico, realiza un Pull Request a su fork (**NO al repositorio de la cátedra**) y agrega al docente como colaborador
1. Las correcciones se seguirán desde la plataforma de la Pull Request.
1. Todas las dudas deberán expresarse como Issues en el repositorio de prácticas con el formato 'TP{Nro} - Titutlo' y en el cuerpo del issue deberán especificar su duda. De esta manera la explicación quedará disponible para todos los equipos.
