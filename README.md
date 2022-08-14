# Formulario **"Datos_Asignaturas_Inv"** implementado en Django

Usando datos en un [archivo CSV](https://espinosadvlpr.github.io/Datos_Asignaturas_Inv_U.csv) de una encuesta aplicada a estudiantes de ingenieria se realizo un desarrollo en el lenguaje de programación **Python** usando el framework **Django** para implementar esa misma encuenta ademas de guardar el CSV y los nuevos registros en una base de datos. Dentro del proyecto se realizo la creación de reportes usando la libreria [Highcharts](https://www.highcharts.com/) para paginas web, en este momento el dashboard cuenta con 3 reportes: diagrama de barras con los estudiantes que viven en cada ciudad, diagrama de dispersión con la cantidad de estudiantes agrupados por edad y diagrama de dona con el porcentaje de vivienda de los estudiantes.

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

Edite la configuración de usuario y contraseña de `MySQL` para la conexion de la base de datos en la linea 82 del archivo `django_form/settings.py`

`NOTA: En su base de datos MySQL debe ejecutar el comando **create database gestion_datos;** para que el ejercicio funcione correctamente.`

Una vez cambiada la información para la conexión a la base de datos y las librerias necesarias esten instaladas, debe realizar lo siguiente para la migración de las tablas a la base de datos `gestion_datos` creada previamente en **MySQL**

```
$ python manage.py makemigrations
$ python manage.py migrate
```

Para realizar la inserción de los datos, edite la configuración de usuario y contraseña de la base de datos para la conexion de la con **MySQL** en la linea 13 del script `insert_data_db.py`

Ejecutando el script con el siguiente comando se realizara la inserción de los datos en **MySQL**

`
$ python insert_data_db.py
`

Para ejecutar el proyecto de **Django** debe usar el siguiente comando

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
