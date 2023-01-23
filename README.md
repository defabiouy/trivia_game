# Trivia de preguntas y respuestas

Juego realizado como proyecto final del curso de Python, utilizando Flask, Flask-wtf (forms), SQLAlchemy y una BD SQLite.

# Como ejecutarlo:
En el directorio raíz se encuentran la **base de datos** y el **populate.py**.
Para correr el populate y cargar la base de datos, en una consola ejecutar:

    python3 populate.py

Para levantar flask, en una consola ejecutar:

    export FLASK_APP=trivia.py
    export FLASK_ENV=development
    python3 -m flask run


# Pendientes/mejoras:
- Debido a problemas con las funciones provistas por datetime, el formateo del tiempo (para mostrar el tiempo insumido por el jugador) se hizo artesanalmente.
- Cualquiera sea el error ocurrido, siempre se tira un error 500.
- En la BD debería cargar mas datos de pruebas.
- No se usa CSS para los estilos.
