# Valley Route backend

## Descripicón

Este proyecto es un backend desarrollado en Python con el framework FastAPI para la creación de una API REST que permite la gestión de usuarios y la creación de nuevos paquetes, rutas y actividades para cada uno de los usuarios creados en la aplicación. 

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

## Author

Santiago Castro - Desarrollador de software y estudiante de ingeniería de sistemas en la Universidad Nacional de Colombia.


[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=flat-square&logo=github)](https://github.com/sacastrot)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/santiago-castro-tabares/)
[![Stack Overflow](https://img.shields.io/badge/Stack%20Overflow-Profile-blue?style=flat-square&logo=stackoverflow)](https://stackoverflow.com/users/19891867/santiago)

