# Django Project

## Instalacion

Para levantar el entorno seguir los siguientes pasos:

1. clonar el repositorio
1. crear entorno: `python3 -m venv ./venv`
1. activar entorno: `source ./venv/bin/activate`
1. instalar requerimientos: `pip install -r requirements.txt`
1. Instalar memcache https://github.com/memcached/memcached/wiki/Install 
1. crear base de datos Mysql y asignar permisos:
* **Crear base de datos:** `CREATE DATABASE IF NOT EXISTS djangodb CHARACTER SET = 'utf8';`
* **Agregar usuario:** `CREATE USER 'dario'@'localhost' IDENTIFIED BY 'Password123#@!';`
* **Asignar todos los permisos:** `GRANT ALL PRIVILEGES ON *.* TO 'dario'@'localhost';`
* **Asignar todos los permisos:** ` GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP
    -> ON djangodb.*
    -> TO 'dario'@'localhost';`
1. `python manage.py migrate` 
1. `python manage.py makemigrations`     
    
---

