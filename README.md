#  GildedRose

## Introducción
El famoso negocio de Ollivander ha crecido. Antes consistía en esto:

Como la demanda de productos mágicos no para de crecer, la expansión del negocio es inevitable para sobrevivir a Amazon.

Ollivander había contratado a Dobbie -a través del programa de FP Dual DAW de Hogwarts colegio concertado- para que le hiciese una app que gestionase el inventario, pero tras los tristes acontecimientos en los que se vió -desgraciadamente- envuelto el pobrecico elfo, no tiene a nadie que pueda modificar el código para incluir nuevos productos.
Implementa las historias de usuario de las GUI proporcionadas en la carpeta historias de usuaria GUI, pero en ASCII.

Ollivander ha contratado los servicios de la consultora en la que trabajas para que adecúe la aplicación a las nuevas necesidades del inventario, por lo que te envían "a cliente" -a la tienda- a lidiar con él y, lo que es peor, con el código spagheti que manufacturó Dobby en sus momentos de langidez infinita.

Por si no fuera suficiente, tu compañero de empresa al que enviaron a cliente antes que a ti, acaba de irse de España porque en el extranjero le pagan por trabajar, y ha dejado tiritando el código de los casos test que intentó añadir en un día de desesperación absoluta.

## Database
- He utilizado PostgreSQL, ya que lo habíamos utilizado en la asignatura de base de datos.


## Docker
- He creado un Docker Compose para definir múltiples contenedores en una aplicación y facilitar la gestión de la infraestructura.

## Frontend
- HTML, BOOSTRAP, CSS, JAVASCRIPT VANILLA

## Backend
- Python, Flask

## Estructura
- db:
  - db.py
    - Conexión con la base de datos 
- domain:
  - aged_brie.py, backstage.py, conjured_item.py, gilded_rose.py, interfaz.py, item.py, normal_item.py, sulfuras.py
    - Todos los items con sus respectivos metodos para el quality y el sellin
- models:
  - product_model.py
    - Realización de las querys a la base de datos para los diferentes requests.
- models/entities:
  - product.py:
    - Para la creación de los produtos y convertir las respuestas en JSON
- routes:
  - product.py:
    - Creación de las rutas aplicando la query correspondiente a cada una de ellas.
- static
  - index.html:
    - Frontend de la página aplicando boostrap
  - styles.css:
    - Maquetación de la página
  - script.js:
    - Realización del CRUD sobre la página del frontend.

## Funcionalidades

Mi proyecto utiliza una base de datos con diferentes productos, incluyendo información sobre calidad y caducidad. El proyecto cuenta con una API REST que permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en los productos. Además, se puede acceder a este CRUD tanto desde el cliente Postman como desde el frontend:

1. Crear producto: Permite agregar un nuevo producto a la base de datos, proporcionando información sobre su nombre, calidad y fecha de caducidad.

2. Leer productos: Permite obtener la lista de todos los productos almacenados en la base de datos, incluyendo detalles como el nombre, calidad y fecha de caducidad de cada uno.

3. Actualizar producto: Permite modificar la información de un producto existente, como su nombre, calidad o fecha de caducidad.

4. Eliminar producto: Permite eliminar un producto de la base de datos en función de su identificador único.


## Instalación
1. Clonar el proyecto
2. Ejecutar:
```docker compose up```


## Créditos

Este proyecto a sido creado por Manuel Ortega.

## Contacto
Github: https://github.com/ManuOrt/Sneaker_Raffle

Email: mortegamarti@cifpfbmoll.eu


