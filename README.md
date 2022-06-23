## Configuración Inicial
1. Instalar XAMPP (en caso de ser necesario se debe agregar mysql al Path)
2. Inicializar el servicio de msyql desde la aplicación de XAMPP
2. Instalar Python
3. Clonar repositorio

~~~
git clone url_de_repositorio
~~~

4. Moverse a la carpeta del repositorio

~~~
cd nombre_de_carpeta_de_repositorio
~~~

5. Crear entorno virtual
~~~
python -m venv env
~~~

6. Activar entorno virtual

~~~
env/Scripts/activate
~~~

7. Instalar requirements.txt

~~~
pip install -r requirements.txt
~~~

8. Crear base de datos(La terminal debe ser de tipo command prompt o CMD)

~~~
mysql -u root -h localhost -p < ./DB/script.sql
~~~


9. Moverse a la carpeta en la cual se encuentra ./manage.py

~~~
cd libreria
~~~

10. Crear migraciones

~~~
python libreria/manage.py makemigrations
~~~

11. Ejecutar migraciones

~~~
python libreria/manage.py migrate
~~~

12. Ejecutar servidor

~~~
python libreria/manage.py runserver
~~~

## Ejecución posterior a la configuración inicial
1. Activar entorno virtual

~~~
env/Scripts/activate
~~~

2. Inicializar el servicio de msyql desde la aplicación de XAMPP

3. Moverse a la carpeta en la cual se encuentra ./manage.py

~~~
cd libreria
~~~

4. Ejecutar servidor

~~~
python libreria/manage.py runserver
~~~

## En caso de ser necesario reconstruir la base de datos

1. Inicializar el servicio de msyql desde la aplicación de XAMPP

2. Entramos a mysql

~~~
mysql -u root -h localhost -p
~~~

3. Borramos la base de datos(en nuestro caso especifico la base de datos se llama libreria)

~~~
drop database libreria;
~~~

4. salimos de mysql

~~~
exit;
~~~

5. Volvemos a construir la base de datos(si el comando falla es probable que estes en una carpeta distinta a la esperada y por tanto deben modificar la ruta hacia el archivo script.sql)
~~~
mysql -u root -h localhost -p < ./DB/script.sql
~~~
 