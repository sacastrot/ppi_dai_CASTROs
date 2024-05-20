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
- Iniciar sesión.
- Cambiar la contraseña.
- Crear un paquete.
- Obtener los paquetes de un usuario.
- Obtener un paquete por su id.
- Obtener los nodos de un paquete.
- Obtener las aristas de un paquete.
- Obtener todos los nodos.
- Obtener todas las aristas.
- Crear un nodo.
- Crear una arista.
- Obtener estadísticas de la aplicación.

Puede acceder a la documentación de la API en el siguiente enlace: [Documentación de la API](https://ppi-dai-castros.onrender.com/docs)

## Autor

Santiago Castro - Desarrollador de software y estudiante de ingeniería de sistemas en la Universidad Nacional de Colombia.


[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=flat-square&logo=github)](https://github.com/sacastrot)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/santiago-castro-tabares/)
[![Stack Overflow](https://img.shields.io/badge/Stack%20Overflow-Profile-blue?style=flat-square&logo=stackoverflow)](https://stackoverflow.com/users/19891867/santiago)

