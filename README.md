# ValleyRoute

## Tabla de Contenido
1. [Descripción](#descripción)
2. [Justificación](#justificación)
3. [Uso de las librerías](#uso-de-las-librerías)
4. [Sitio Web](#sitio-web)
    - [Frontend](#frontend)
    - [Backend](#backend)
        - [Endpoints](#endpoints)
5. [Autor](#autor)


## Descripción
ValleyRoute es una aplicación de rastreo de envíos que permite a los usuarios seguir el estado y la ubicación de sus paquetes dentro del área metropolitana del Valle de Aburrá en Antioquia, Colombia. La aplicación ofrece detalles precisos sobre el progreso de los envíos y la ruta que ha seguido entre los nodos que tiene la empresa de envíos.

## Justificación
Con el continuo crecimiento de las compras en línea y el comercio eléctronico, los consumidores demandan transparencia y actualizaciones en tiempo real sobre sus envíos. ValleyRoute busca satisfacer esta necesidad al proporcionar una herramienta para hacer el seguimiento de envíos, específicamente diseñada para el área metropolitana del Valle de Aburrá.

## Uso de las Librerías
- **NumPy:** Utilizado para el manejo eficiente de datos relacionados con la logística y los envíos.
- **Pandas:** Para la manipulación y análisis de datos estructurados, como registros de seguimiento de envíos y rutas.
- **Matplotlib:** Creación de visualizaciones interactivas y gráficos para mostrar estdadísticas de los envíos.
- **Scipy:** Para cálculos estadísticos y optimización de rutas de envío basadas en datos históricos, así como para el cálculo de la ruta más eficiente utilizando el algoritmo de Dijkstra dentro del área metropolitana del Valle de Aburrá.
- **Geopandas:** Integración de datos geoespaciales para representar la ubicación de los envíos en mapas, centrándose en el área del Valle de Aburrá.

## Sitio Web

### Frontend
El proyecto ValleyRoute cuenta con un sitio web que permite a los usuarios:

- Registrarse y autenticarse para acceder al sitio web
- Cambiar la contraseña de su cuenta
- Visualizar la ruta más optima que va a seguir su envío
- Crear nuevos paquetes y asignar un destino y un final
- Visualizar estadísticas de los envíos
- Visualizar todos los paquetes que ha creado con la cuenta creada


El sitio web se encuentra en la siguiente dirección: [ValleyRoute](http://valleyweb.s3-website-us-east-1.amazonaws.com/)

El repositorio del frontend se encuentra en la siguiente dirección: [ValleyRoute Frontend](https://github.com/sacastrot/valley-route-f)

### Backend

El backend de ValleyRoute es una API REST desarrollada en Python con el framework FastAPI. La API se encarga de gestionar los datos de los usuarios, paquetes, nodos y aristas de la aplicación. Además, se encarga de calcular la ruta más corta entre dos puntos de control de la empresa de envíos y la distancia recorrida entre ellos.

El backend se encuentra en la siguiente dirección: [ValleyRoute API](https://ppi-dai-castros.onrender.com/docs)

El código fuente del backend se encuentra en la carpeta `valley_route-b` de este repositorio.

- Creación del grafo con los puntos de control de la empresa (pandas, numpy, geopandas)


![valley_route_graph](https://github.com/sacastrot/ppi_dai_CASTROs/assets/70394887/d9a3929e-0520-4fec-8c14-cb7ece4f0f1d)

- Funciones para el caculo de la ruta más corta entre dos puntos de control dados (Scipy, pandas, numpy)
- Funciones para conocer la distancia recorrida entre dos puntos de control dados (pandas, numpy)

La API tiene las siguientes funciones:

#### Endpoints

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

## Autor

Santiago Castro - Desarrollador de software y estudiante de ingeniería de sistemas en la Universidad Nacional de Colombia.


[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=flat-square&logo=github)](https://github.com/sacastrot)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/santiago-castro-tabares/)
[![Stack Overflow](https://img.shields.io/badge/Stack%20Overflow-Profile-blue?style=flat-square&logo=stackoverflow)](https://stackoverflow.com/users/19891867/santiago)


