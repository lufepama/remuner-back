# remuner-back
Para correr en local es necesario seguir los siguientes pasos:
1. Clonar el repositorio
2. Acceder a la ruta raiz del proyecto
3. Instalar las dependencias lanzando => pip install -r requirements.txt   (RECOMENDABLE ACTIVAR ENTORNO VIRTUAL)
4. El proyecto usa PostgreSQL. Es necesario crear la tabla llamada "remuner"
5. Levantar el servidor en local lanzando el siguiente comando en la terminal => uvicorn main:app --reload
