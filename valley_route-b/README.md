# Valley Route backend

## Descripicón

Este proyecto es un backend desarrollado en Python con el framework FastAPI para la creación
de una API REST que permite la gestión de usuarios y la creación de nuevos paquetes, 
rutas y actividades para cada uno de los usuarios creados en la aplicación.

Se puede acceder a la API en el siguiente
enlace: [Documentación de la API](https://ppi-dai-castros.onrender.com)

## Tecnologías

- [Python](https://www.python.org/) - Lenguaje de programación utilizado. (3.10)
- [FastAPI](https://fastapi.tiangolo.com/) - Framework utilizado para la creación de la API.
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Librería utilizada para la validación de datos.
- [SQLAlchemy](https://www.sqlalchemy.org/) - Librería utilizada para la conexión con la base de datos.
- [PostgreSQL](https://www.postgresql.org/) - Base de datos utilizada para el almacenamiento de los datos.
- [Docker](https://www.docker.com/) - Tecnología utilizada para la creación de contenedores. 

## Instalación

Para instalar el proyecto en tu máquina local, sigue los siguientes pasos:

1. Clona el repositorio en tu máquina local.  
```
git clone https://github.com/sacastrot/ppi_dai_CASTROs.git
```
2. Crea un entorno virtual en la raíz del proyecto.
3. Activa el entorno virtual.
4. Instala las dependencias del proyecto.
```
pip install -r requirements.txt
```
5. En el archivo config.py cambia la url de la base de datos por la url de tu base de datos.
6. Ejecuta el proyecto.
```
uvicorn main:app --reload
```
7. Accede a la documentación de la API en tu navegador, según el puerto configurado.  
```
http://localhost:8000/docs
```

## Base de datos

Para la creación de la base de datos se utilizó PostgreSQL. La base de datos tiene
las siguientes tablas:

- user
- package
- node
- edge

### Relaciones

Las relaciones entre las tablas son las siguientes:

- Un usuario puede tener muchos paquetes.
- Un paquete tiene un nodo inicial y un nodo final.
- Un nodo puede tener muchas aristas.
- Una arista tiene un nodo origen y un nodo destino.

### Tabla user

| Campo | Tipo | Descripción                        |
| --- | --- |------------------------------------|
| id | Integer | Identificador único del usuario.   |
| firstName | String | Primer nombre del usuario          |
| lastName | String | Apellido del usuario               |
| email | String | Correo electrónico del usuario     |
| password | String | Contraseña del usuario, encriptada |
| is_active | Boolean | Indica si el usuario está activo  |

### Tabla package
| Campo | Tipo | Descripción                        |
| --- | --- |------------------------------------|
| id | Integer | Identificador único del paquete.   |
| description | String | Descripción del paquete          |
| created_at | DateTime | Fecha de creación del paquete    |
| user_id | Integer | Identificador del usuario que creó el paquete |
| start_node_id | Integer | Identificador del nodo inicial del paquete |
| end_node_id | Integer | Identificador del nodo final del paquete |

### Tabla node
| Campo | Tipo | Descripción                        |
|-------| --- |------------------------------------|
| id    | Integer | Identificador único del nodo.      |
| name  | String | Nombre del nodo                    |
| lat   | Float | Latitud del nodo                  |
| lng   | Float | Longitud del nodo                  |

### Tabla edge
| Campo | Tipo | Descripción                        |
|-------| --- |------------------------------------|
| id    | Integer | Identificador único de la arista.  |
| start_node_id | Integer | Identificador del nodo origen de la arista |
| end_node_id | Integer | Identificador del nodo destino de la arista |
| distance | Float | Distancia entre los nodos         |

## Estructura de archivos

- **app**: Contiene los archivos de la aplicación.
  - **__init__**: Archivo de inicialización de la aplicación.
  - **auth**: Contiene todas las rutas relacionadas con la autenticación de 
  los usuarios. Y las funciones necesarias para la autenticación.
  - **crud**: Contiene las funciones necesarias para la creación, lectura,
    actualización y eliminación de los datos en la base de datos.
  - **database**: Contiene los archivos necesarios para la conexión con la base de datos.
  - **main**: En este archivo se encuentra la configuración de la aplicación y las rutas de la API. Y se ejecuta la aplicación.
  - **models**: Contiene las clases de los modelos de la base de datos.
  - **schemas**: Contiene las clases de los esquemas de los modelos. Que permiten la validación de los datos.
- **.gitignore**: Archivo que contiene los archivos y carpetas que se deben ignorar en el repositorio.
- **config.py**: Archivo que contiene la configuración de la base de datos.
- **docker-compose.yml**: Archivo de configuración de Docker. Para ejecutar la aplicación en un contenedor con una base de datos PostgreSQL local.
- **Dockerfile**: Archivo de configuración de Docker. Para la creación de la imagen de la aplicación. Esta imágen se puede ejecutar en un contenedor, para facilitar la ejecución de la aplicación y su despliegue.
- **requirements.txt**: Archivo que contiene las dependencias del proyecto.
- **README.md**: Archivo que contiene la información del proyecto.

## Rutas
Desde la documentación de la API se pueden realizar las siguientes acciones:

- Crear un usuario.

| Método | URL | Descripción |
| ------ | --- | ----------- |
| POST | /auth/ | Crear un usuario en la plataforma, <br> No requiere estar autenticado |


- Iniciar sesión.

| Método | URL | Descripción |
| ------ | --- | ----------- |
| POST | /auth/token/ | Iniciar sesión en la plataforma, <br> retorna un token JWT, <br> No requiere estar autenticado |

- Cambiar la contraseña.

| Método | URL | Descripción |
| ------ | --- | ----------- |
| POST | /auth/reset-password/ | Cambiar la contraseña de un usuario, <br> No requiere estar autenticado |


- Obtener información de un usuario

| Método | URL | Descripción |
| ------ | --- | ----------- |
| GET | / (Ruta raíz) | Obtener la información de un usuario, <br> Requiere estar autenticado |

- Obtener todos los nodos de la empresa

| Método | URL | Descripción |
| ------ | --- | ----------- |
| GET | /node/ | Obtener todos los nodos de la empresa, <br> Requiere estar autenticado |

- Crear un nodo de la empresa

| Método | URL | Descripción |
| ------ | --- | ----------- |
| POST | /node/ | Crear un nodo de la empresa, <br> Requiere estar autenticado |

- Obtener todas las conexiones de los puntos de control (aristas del grafo) de la empresa

| Método | URL | Descripción |
| ------ | --- | ----------- |
| GET | /edge/ | Obtener todas las conexiones de los puntos de control, <br> Requiere estar autenticado |

- Crear una conexión entre dos puntos de control (arista del grafo)

| Método | URL | Descripción |
| ------ | --- | ----------- |
| POST | /edge/ | Crear una conexión entre dos puntos de control, <br> Requiere estar autenticado |

- Crear un paquete

| Método | URL | Descripción |
| ------ | --- | ----------- |
| POST | /package/ | Crear un paquete, <br> Requiere estar autenticado |

- Obtener un paquete

| Método | URL | Descripción |
| ------ | --- | ----------- |
| GET | /package/{package_id} | Obtener un paquete, regresa la ruta óptima que va a seguir el paquete <br> Requiere estar autenticado |

- Obtener todos los paquetes de un usuario

| Método | URL | Descripción |
| ------ | --- | ----------- |
| GET | /packages | Obtener todos los paquetes de un usuario, solo la información básica <br> Requiere estar autenticado |

- Obtener estadísticas de los nodos de inicio de la empresa

| Método | URL | Descripción |
| ------ | --- | ----------- |
| GET | /statistics/nodestart | Obtener estadísticas de los nodos de inicio de la empresa, <br> no requiere estar autenticado |

- Obtener estadísticas de los nodos de final de la empresa

| Método | URL | Descripción |
| ------ | --- | ----------- |
| GET | /statistics/nodeend | Obtener estadísticas de los nodos de final de la empresa, <br> no requiere estar autenticado |


Puede acceder a la documentación de la API en el siguiente enlace: [Documentación de la API](https://ppi-dai-castros.onrender.com/docs)

## Autor

Santiago Castro - Desarrollador de software y estudiante de ingeniería de sistemas en la Universidad Nacional de Colombia.


[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=flat-square&logo=github)](https://github.com/sacastrot)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/santiago-castro-tabares/)
[![Stack Overflow](https://img.shields.io/badge/Stack%20Overflow-Profile-blue?style=flat-square&logo=stackoverflow)](https://stackoverflow.com/users/19891867/santiago)

