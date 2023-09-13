# remuner-back
Para correr en local es necesario seguir los siguientes pasos:
1. Clona el repositorio.
2. Navega hasta la carpeta principal del proyecto.
3. Instala las dependencias ejecutando el comando pip install -r requirements.txt (se recomienda usar un entorno virtual).
4. Dado que el proyecto utiliza PostgreSQL, es necesario crear la tabla llamada "remuner".
5. Inicia el servidor local con el siguiente comando en la terminal: uvicorn main:app --reload.
6. Para ejecutar las pruebas con pytest, utiliza el siguiente comando: pytest test_file.py.
