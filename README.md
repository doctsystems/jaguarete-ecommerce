# JaguaShop
JaguaShop es un e-commerce desarrollado durante el Bootcamp Desarrollo Web Fullstack con Python y Django - Polotic Misiones 2021.

Aquí aprenderás a manejar la autenticación y el registro de usuarios, a crear secciones internas sólo para usuarios autenticados, perfiles de usuario y lo mejor de todo, un filtrado de productos muy eficiente.

---
## Comenzando 🚀

El sitio web está desarrollado con el framework [Django](https://www.djangoproject.com/) y esta desplegado en un VPS en [Digital Ocean](https://www.digitalocean.com/)

---
## Web site

- [Acceder al sitio](https://jaguarete.diegoosvaldo.me/)

---
## Demo Youtube

- [Review del sitio](https://youtu.be/BC8FKUqcPXQ)

---
## Thumbnail
<img   src="https://jaguarete.diegoosvaldo.me/static/store/images/thumbnail.jpg" />

### Pre-requisitos 📋

_El principal requisito es tener instalado [Python](https://www.python.org/), los demas requisitos estan listados en el archivo requirements.txt_

### Que es lo que hay aqui?

El proyecto contiene 5 apps:

- __Store__ - Nucleo principal del proyecto
- __Producto__ - CRUD de items para el sitio web
- __Users__ - Autenticacion y registro de usuarios
- __Cart__ - Modulo de gestion para el carrito de compras
- __Order__ - CRUD de ordenes y/o pedidos generados por los usuarios

### Que es lo que nos falta?

Aun nos quedan mejoras por hacer:

- __Dashborad__ - CRUD para administracion de usuarios
- __Pasarela__ - Modulo para pagos con APIs de terceros
- __Pedidos__ - Modulo para administracion de pedidos
- __Envios__ - Modulo de tracking de envios
- __Otras__ - Siempre quedan cosas por hacer... 

---
## Instalacion y Configuracion 🔧

### Prerequisitos

- pip package manager 

```
  $ pip --version
  pip 21.1.3
```

### Install 🛠️

- Primero, clonar el repositorio:

```
  git clone https://github.com/doctsystems/jaguarete-ecommerce.git
```

- Acceder a la carpeta del proyecto:

```
  cd ruta-de-la-carpeta
```

- Crear y activar el entorno virtual

```
  $ python -m venv nombre-del-entorno
  $ nombre-del-entorno\scripts\activate (windows)
  $ source nombre-del-entorno/bin/activate (linux)
```

- Instalar dependencias

```
  $ pip install -r requirements.txt
```

### Configuraciones ⚙️

- Configurar la base de datos

```
  'ENGINE': DB.engine,
  'NAME': DB.name,
```

### Running

```
  $ python manage.py makemigrations
  $ python manage.py migrate
  $ python manage.py runserver
```

---
## Despliegue 📦

_Para realizar el despligue te recomiendo seguir la guia de Digital Ocean_

* [Guia de despliegue](https://www.digitalocean.com/community/tutorials/como-configurar-django-con-postgres-nginx-y-gunicorn-en-ubuntu-18-04-es) - Cómo configurar Django con Postgres, Nginx y Gunicorn en Ubuntu 18.04

---
## Desarrollado con 🛠️

_Herramientas y Tecnologias que se utilizaron para el desarrollo del proyecto_

* [Python](https://www.python.org/) - Lenguaje principal
* [Django](https://www.djangoproject.com/) - Para el Backend 
* [HTML](https://es.wikipedia.org/wiki/HTML), [CSS](https://www.w3schools.com/css/) y [JavaScript](https://developer.mozilla.org/es/docs/Web/JavaScript) - Para el Frontend
* [DigitalOcean](https://www.digitalocean.com/) - VPS de despliegue
* [SublimeText](https://www.sublimetext.com/3) - Editor de texto
* [GitHub](https://www.github.com/) - Repositorio del proyecto

---
## Contribuyendo 🖇️

Por favor envie un correo a [d.cruz@outlook.com](mailto:d.cruz@outlook.com) para detalles sobre el código y el proceso para enviar pull requests.

---
## Wiki 📖

Aun no está creada la _Wiki_ del proyecto, te agradeceria mucho que me puedas ayudar a crearla.

---
## Autores ✒️

_Por ahora solo existe un autor y/o desarrollador_

* **Diego Osvaldo** - [Desarrollador Web](https://diegoosvaldo.me/)

---
## Licencia 📄

Este proyecto está desarrollado bajo la Licencia (MIT) - mira el archivo [LICENSE](LICENSE) para más detalles.

---
## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* [Invitame](https://paypal.me/diegoosvaldo85?locale.x=es_XC) una cerveza 🍺 o un café ☕.
* Da las gracias públicamente 🤓.
* etc.

---
⌨️ con ❤️ 😊
