# Formulario **"Datos_Asignaturas_Inv"** implementado en Django

Usando datos en CSV de una encuesta aplicada a estudiantes de ingenieria se realizo un desarrollo en el lenguaje de programación **Python** usando el framework **Django** para implementar esa misma encuenta ademas de guardar el CSV y los nuevos registros en una base de datos sobre la cual se realizaron 3 reportes, diagrama de barras con los estudiantes que viven en cada ciudad, diagrama de dispersión con la cantidad de estudiantes para grupos de edad y diagrama de dona con el porcentaje de vivienda de los estudiantes.

## Requisitos de ejecución del proyecto

Para poder ejecutar correctamente el proyecto es necesario tener instalando `Python`, ademas de un servidor de bases de datos como `MySQL o MariaDB`.


## Instalando el proyecto

Realice la clonación del repositorio usando el comando

`
$ https://github.com/espinosadvlpr/django-form-and-reports.git
`

Realice la instalación de las librerias necesarias para la ejecución del proyecto usando el comando

`
$ pip install -r requirements.txt
`

Edite la configuración de usuario y contraseña de la base de datos para la conexion de la base de datos en la linea 14 del script `insert_data_db.py`

Realice la creación de la base de datos y la inserción de los datos ejecutando el script de creación con el siguiente comando

`
$ python insert_data_db.py
`

Edite la configuración de usuario y contraseña de la base de datos para la conexion de la base de datos en la linea 82 del archivo `django_form/settings.py`

Una vez creada la base de datos correctamente y las librerias necesarias esten instaladas, debe realizar lo siguiente en caso de ser necesario

`
$ python manage.py makemigrations
$ python manage.py migrate
`

Para ejecutar el proyecto

`
$ python manage.py runserver
`

## Navegando por el proyecto

Para ingresar al formulario en el navegador ingrese el siguiente link <http://127.0.0.1:8000/>

Para ingresar al dashboard de reportes en el navegador ingrese el siguiente link <http://127.0.0.1:8000/dashboard>

Si desea revisar los datos subidos al proyecto lo puede realizar desde el `admin`

Primero cree un usuario administrador con el comando

`
$ python manage.py createsuperuser
`

Una vez creado el usuario, para ingresar al `admin` en el navegador ingrese el siguiente link <http://127.0.0.1:8000/admin> en el apartado `Surveys` como se ve en la imagen

![image](https://user-images.githubusercontent.com/38819699/184517885-8309db88-6c2c-44ee-8bd5-b9cf156ddaab.png)

## Evidencias

Si todo ha funcionado correctamente el formulario se deberia ver de la siguiente manera

![image](https://user-images.githubusercontent.com/38819699/184517903-de107c6a-8b0b-415e-8989-1e8259a4ca89.png)

El dashboard de reportes se deberia ver de la siguiente manera

![image](https://user-images.githubusercontent.com/38819699/184517914-f844f4ae-669f-4f3c-ad2c-f978b7f3f311.png)

Y cada uno de los reportes de deberia ver asi

![image](https://user-images.githubusercontent.com/38819699/184517917-17fb2960-3462-4e58-98d9-c61e3ca38bfd.png)
![image](https://user-images.githubusercontent.com/38819699/184517920-868c5ce9-e75f-4279-9915-ae92e652e1cf.png)
![image](https://user-images.githubusercontent.com/38819699/184517923-67a08b04-bcab-4180-be52-4704cc13d34a.png)

`
NOTA: El proyecto sigue en desarrollo de reportes.
`

Happy coding! :)
