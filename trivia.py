from app import app, db
from app.models import Categoria, Pregunta, Respuesta
from flask import session
from datetime import datetime


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Categoria': Categoria, 'Pregunta': Pregunta, 'Respuesta': Respuesta}


def inicializar_valores():

    dicc_categorias_estado = {}

    session.clear()
    session['tiempo_inicial'] = datetime.today().timestamp()

    for categoria in Categoria.query.all():
        dicc_categorias_estado.update({categoria.id:False})

    #print("mi diccionario: ", dicc_categorias_estado)
    session['dicc_categorias_estado'] = dicc_categorias_estado



def contadorMinutos():

    inicio = session['tiempo_inicial']
    #print(session['tiempo_inicial'])
    inicioDt = datetime.fromtimestamp(inicio)
    fin = datetime.today()  # Get timezone naive now
    print("tiempo inicio: ", inicioDt, " tiempo fin: ", fin)

    return formatearFecha(int((fin - inicioDt).seconds))


def formatearFecha(d):
    minutos = d//60
    if minutos > 59:
        horas =  minutos//60
        minutos = minutos%60
    else:
        horas = 0

    segundos = d%60

    print(minutos, ":",segundos)

    if horas < 10:
        horaString = "0"+str(horas)
    else:
        horaString = str(horas)
    if minutos < 10:
        minutosString = "0"+str(minutos)
    else:
        minutosString = str(minutos)

    if segundos < 10:
        segundosString = "0"+str(segundos)
    else:
        segundosString = str(segundos)

    #print(horaString + ":" + minutosString + ":" + segundosString)
    return (horaString + ":" + minutosString + ":" + segundosString)



# sigo este ejemplo: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms


'''
los ejemplos de linea de comandos se tiran desde:
d444911@Y4308567 ~/workspace/springBoot/python_a_distancia/src $ python3
Python 3.4.3 (default, Oct 14 2015, 20:28:29) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from app.models import User
>>> u = User(username='susan', email='susan@example.com')
>>> u
<User susan>
>>> 

'''