# PROYECTO:MÓDULO VIII - DOCKER DJANGO
1. Propósito: Demostrar los conocimientos adquiridos en la creación de un proyecto en
Django.
2. Requerimientos:
- Desplegar tu aplicación en Django, que fue desarrollado en módulo 5, utilizando docker-compose. 
- Subir el docker-compose.yml y Dockerfie en tu repositorio de github (si la aplicación fue desarrollado en grupo, hacer un fork del repositorio común y enviar una separada) 
- levantar un nexus repository en una VM,  desplegar tu aplicación en otra VM descargando la imagen docker de la aplicación desde el nexus
- ->Enviar la URL del tu repositorio.
- ->enviar un video del cuándo se despliega tu aplicación utilizando nexus repository


# Members
1. Edy Felix Tarqui Guarachi  
2. Elmer Mamani Ticona
Este README, cuenta con los pasos para levantar en ambientes de desarrollo la App de MiniKardex, desarrollado con Python v3.9 y Django v4.1.2
### Pasos docker ###
```commandline
docker compose up -d 
```
## APP DE MINIKARDEX ##
### Requisitos ###

* Python 3.9.11 o superior

### Pasos ###

* Crear entorno virtual
* Instalar los requirements para la App.
```commandline
pip install -r requirements.txt
```
* Correr la App 
```commandline
python manage.py runserver
```
### Usuario de prueba ###
```commandline
username: usertest
password: 4rch12022
```
### Url de acceso en el Navegador
```commandline
http://localhost:8000/minikardex
```
### Django REST Framework
* EndPoint Tipo de Productos
```commandline
Method: [GET]
Url: http://localhost:8000/api/producto/tipoproducto/
Response:
[
    {
        "id": 1,
        "tipoproducto": "TASAS",
        "descripcion": "TASAS"
    },
    {
        "id": 2,
        "tipoproducto": "JUGUETES",
        "descripcion": "JUGUETES"
    },
    {
        "id": 3,
        "tipoproducto": "POLERAS",
        "descripcion": "POLERAS DE SUPER HEROES"
    }
]
```
* EndPoint Categoria de productos
```commandline
Method: [GET]
Url: http://localhost:8000/api/producto/categoria/
Response:
[
    {
        "id": 1,
        "categoria": "DC COMICS",
        "descripcion": "DC COMICS"
    },
    {
        "id": 2,
        "categoria": "MARVEL",
        "descripcion": "MARVEL"
    }
]
```
* Productos
```commandline
Method: [GET]
Url: http://localhost:8000/api/producto/producto/
Response:
[
    {
        "id": 1,
        "categoria": {
            "id": 1,
            "categoria": "DC COMICS",
            "descripcion": "DC COMICS"
        },
        "categoria_id": 1,
        "tipoproducto": {
            "id": 1,
            "tipoproducto": "TASAS",
            "descripcion": "TASAS"
        },
        "tipoproducto_id": 1,
        "producto": "TASA BATMAN",
        "descripcion": "TASA BATMAN COLOR BLANCO Y NEGRO",
        "imagen": "http://localhost:8000/media/productos/BATMAN_TASA.jpg",
        "stock": 26,
        "precio": "15.00",
        "estado": true
    },
    {
        "id": 2,
        "categoria": {
            "id": 2,
            "categoria": "MARVEL",
            "descripcion": "MARVEL"
        },
        "categoria_id": 2,
        "tipoproducto": {
            "id": 3,
            "tipoproducto": "POLERAS",
            "descripcion": "POLERAS DE SUPER HEROES"
        },
        "tipoproducto_id": 3,
        "producto": "POLERA IRON MAN ROJO",
        "descripcion": "POLERA IRON MAN ROJO TALLA XL",
        "imagen": "http://localhost:8000/media/productos/IRONMAN.jpg",
        "stock": 63,
        "precio": "41.00",
        "estado": true
    }
]
```
### Capturas de Pantalla
* Productos
![Produtos](https://github.com/eajahuanca/minikardex/blob/main/capturas/Productos.JPG "Productos")
![Formulario Productos](https://github.com/eajahuanca/minikardex/blob/main/capturas/ProductoForm.JPG "Formulario de Producto")
* Ingresos
![Ingresos](https://github.com/eajahuanca/minikardex/blob/main/capturas/Ingresos.JPG "Ingresos")
![Formulario Ingresos](https://github.com/eajahuanca/minikardex/blob/main/capturas/IngresoForm.JPG "Formulario de Ingresos")
* Ventas
![Ventas](https://github.com/eajahuanca/minikardex/blob/main/capturas/Ventas.JPG "Ventas")
![Formulario Ventas](https://github.com/eajahuanca/minikardex/blob/main/capturas/VentaForm.JPG "Formulario de Ventas")
