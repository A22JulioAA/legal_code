# Estructura de directorios y archivos

A continuación se documentará la estructura de directorios y archivos y su función en el proyecto. Aclarar previamente que se trata de una aplicación construida con Django, framework de Python, así como Javascript, HTML y CSS. Cada una de estas tecnologías añaden a mayores librerías, módulos etc.

Comenzamos con un esquema general de los directorios y los archivos de la raíz del proyecto:

​	

```
- assets/
- citas/
- comentarios/
- core/
- legal_code/
- media/
- node_modules/
- static/
- users/
- .env(produccion)
- .gitignore
- manage.py
- package-lock.json
- package.json
- README.md
- requirements.txt
- webpack.config.js
```

A continuación una explicación de cada elemento y los elementos interiores de los directorios:

### assets/

```
- scripts/
- styles/
```

Este directorio contiene dos directorios más. Como sus nombres indican uno almacena scripts y otro hojas de estilos. La finalidad de tener un **assets/ ** es  crear dentro los archivos que luego van a ser minificados por el webpack para reducir su tamaño. El resultado de este proceso se enviará a **static/**.

### citas/

```
- migrations/
- templates/
- __init__.py
- admin.py
- apps.py
- forms.py
- models.py
- tests.py
- urls.py
- views.py
```

Este directorio representa una **aplicación de Django**. Las aplicaciones son módulos que se crean con la intención de realizar una tarea específica en el proyecto. En este caso lo que hace es almacenar diferentes elementos relacionados con las tareas de *citas*. La estructura es más o menos la misma que en todas las aplicaciones: **migrations/** es un directorio donde se almacenan las migraciones de la base de datos; **templates/** es otro directorio donde se almacenan las plantillas usadas para las citas(*agendar_cita* y *citas_principal*); **admin.py** se usa para gestionar el panel de administración incorporado por Django con respecto a esta apicación; **apps.py** se usa para configurar la aplicación, pudiendo incluirse diferentes opciones deseadas por el desarrollador; **forms.py** sirve para, como su propio nombre indica, crear los formularios que se usarán en la aplicación; **models.py** sirve para almacenar los modelos que creamos para, en este caso, las citas en la base de datos; **test.py** nos sirve para crear pruebas unitarias de la aplicación; **urls.py** contiene las rutas que componen este apartado, teniendo exclusivamente las relacionadas con las citas, ya que luego se incluyen todas en la aplicación principal; **views.py** se usa para almacenar las vistas de la aplicación, y contiene toda la lógica, llamadas a templates y demás procesos que hacen que la página sea dinámica y use la base de datos.

### comentarios/

```
- migrations/
- __init__.py
- admin.py
- apps.py
- forms.py
- models.py
- tests.py
- urls.py
- views.py
```

Este directorio representa la aplicación de *comentarios* y almacena el código necesario para gestionarlos e implementarlos con el resto del código. Evitando la repetición, los directorios interiores son los mismos y con su misma funcionalidad, excepto **templates/**, que no existe en *comentarios*. En este caso no se hace uso de ninguna plantilla y se trata todo desde la aplicación principal.

### core/

```
- migrations/
- templates/
- __init__.py
- admin.py
- apps.py
- forms.py
- models.py
- tests.py
- urls.py
- views.py
```

Probablemente el directorio más complejo del proyecto. Es la parte central (core) de la aplicación y es donde desembocan el resto de módulos. Como se ha comentado anteriormente, los archivos y directorios interiores tienen la misma funcionalidad pero se aclarará la estructura de un directorio en concreto: **templates/** contiene dos subdirectorios, *core* y *registration*. En *core* se almacenan las plantillas relacionadas con la base(plantilla base del resto de páginas), calendario, homepage, politica de cancelaciones y sobre nosotros. En registration se almacenan las plantillas de login y registro.

###   legal_code/

```
- __init__.py
- asgi.py
- settings.py
- urls.py
- views.py
- wsgi.py
```

El verdadero núcleo de la aplicación y el principal directorio del proyecto. En el se establece la configuración con la base de datos, el middleware, conexiones con directorios etc(**settings.py**). Todas las urls contenidas en los **urls.py** de las diferentes aplicaciones se 'importan' aquí, en el propio **urls.py** del directorio. Tanto **asgi.py** como **wsgi.py** son archivos que gesitonan servidores web compatibles, pero no se utilizan en este caso. El archivo **views.py** realiza la misma función que en cualquier aplicación, pero en este caso, como está completamente modularizado el proyecto y, en todo caso, se trata más generalmente en **core/**, no contiene nada.

### media/

En este directorio se almacenan las imágenes o ficheros subidos por los usuarios así como las imágenes de los profesionales. Su función es simple y no hace nada más.

### node_modules/

En este directorio se almacenan las dependencias instaladas con npm. En este proyecto se han instalado algunas librerías de Javascript mediante npm y, por lo tanto, esta carpeta contendrá los archivos de estas instalaciones.

### static/

Este directorio es uno de los más importantes también, pues el contenido de **assets/** mencionado anteriormente termina aquí, más concretamente en el subdirectorio **js/**. Como podemos intuir, en el subdirectorio **css/** se almacenan las hojas de estilo estáticas del proyecto, en el cual tenemos una hoja para base, otra para homepage, otra para profile y otra para sobre nosotros. Finalmente en el subdirectorio **img/** se organizan y almacenan las imágenes que se utilizarán de manera estática, como por ejemplo imágenes de fondo, iconos, logos etc.

### users/

```
- migrations/
- templates/
- __init__.py
- admin.py
- apps.py
- models.py
- tests.py
- urls.py
- views.py
```

Volvemos a la estructura de las anteriores aplicaciones. La única diferencia con ellas es que **users/** almacena los archivos que gestionan los usuarios de la aplicación. No se ha seguido el modelo estándar de Django y en consecuencia se ha creado un nuevo modelo de gestión de usuarios. En este caso el cliente es el usuario y así se refleja en el archivo **models.py**.

### .env

Como ya será sabido por la mayoría, en este fichero se almacenan valores sensibles por contener información sobre bases de datos, configuraciones etc. Se establecen las credenciales de acceso a la base de datos y los host permitidos. Para obtener este archivo es necesario ponerse en contacto con el desarrollador: a22julioaa@iessanclemente.net

### .gitignore

Aquí se establecen qué archivos van a ser ignorados al subir el repositorio Github o Gitlab.

### manage.py

Este archivo es muy importante y necesario. Es un archivo generado automáticamente por Django y que contiene la lógica para ejecutar comandos propios que serán necesarios para desarrollar una aplicación con este framework. Un ejemplo es cargar las migraciones en la base de datos, que en este caso se haría ejecutando lo siguiente:

```bash
python manage.py migrate
```

### package-lock.json y package.json

Son dos archivos generados al instalar dependencias con npm y dentro de ellos se almacenan en forma de json las versiones de estas dependencias, diferentes configuraciones de comandos de npm y alguna información más.

### README.MD

Este es un archivo que contiene la presentación del proyecto y que acompañará a la página principal en el repositorio. 

### requirements.txt

Cuando se desarrolla una aplicación suele hacerse uso de librerías, módulos o demás recursos ofrecidos por el propio lenguaje de programación utilizado y en otros casos por terceros. En nuestro caso se han utilizado numerosas librerías de Python y de Django para desarrollar la página, como por ejemplo 'Crispy Forms', 'Jinja2' o 'Pillow'. Todos estos módulos hay que instalarlos en el equipo o en el entorno donde se vaya a ejecutar la aplicación mediante un instalador de paquetes('pip' en este caso). Para agilizar el proceso se crea este **requirements.txt**, que almacena todos los paquetes y sus correspondientes veriones y luego solo habrá que ejecutar el siguiente comando para que se instalen todos: 

```
pip install -r requirements.txt
```

Esto ayuda mucho a la hora de desplegar la aplicación pues pasaríamos a un solo comando lo que de manera individual serían muchos más.

### webpack.config.js

En este archivo se establece la configuración del webpack, un empaquetador de módulos usado en el proyecto para combinar Javascript, CSS, imágenes y demás de manera sencilla.