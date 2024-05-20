# ValleyRoute

## Tabla de Contenido
1. [Descripción](#descripción)
2. [Justificación](#justificación)
3. [Uso de las librerías](#uso-de-las-librerías)
4. [Sitio Web](#sitio-web)
7. [Author](#author)

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

El repositorio del frontend se encuentra en la siguiente dirección: [ValleyRoute Frontend](https://github.com/sacastrot/valley-route-front)

### Backend

El backend de ValleyRoute es una API REST desarrollada en Python con el framework FastAPI. La API se encarga de gestionar los datos de los usuarios, paquetes, nodos y aristas de la aplicación. Además, se encarga de calcular la ruta más corta entre dos puntos de control de la empresa de envíos y la distancia recorrida entre ellos.

El backend se encuentra en la siguiente dirección: [ValleyRoute API](https://ppi-dai-castros.onrender.com)

El código fuente del backend se encuentra en la carpeta `valley_route-b` de este repositorio.

- Creación del grafo con los puntos de control de la empresa (pandas, numpy, geopandas)


![valley_route_graph](https://github.com/sacastrot/ppi_dai_CASTROs/assets/70394887/d9a3929e-0520-4fec-8c14-cb7ece4f0f1d)

- Funciones para el caculo de la ruta más corta entre dos puntos de control dados (Scipy, pandas, numpy)
- Funciones para conocer la distancia recorrida entre dos puntos de control dados (pandas, numpy)

La API tiene las siguientes funciones:

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


## Author

Santiago Castro - Desarrollador de software y estudiante de ingeniería de sistemas en la Universidad Nacional de Colombia.


[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=flat-square&logo=github)](https://github.com/sacastrot)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/santiago-castro-tabares/)
[![Stack Overflow](https://img.shields.io/badge/Stack%20Overflow-Profile-blue?style=flat-square&logo=stackoverflow)](https://stackoverflow.com/users/19891867/santiago)


