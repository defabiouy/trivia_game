from flask import render_template
from flask import session
from random import randint
from app import app, db
from app.models import Categoria, Pregunta, Respuesta
import trivia



@app.route('/')
@app.route('/trivia', methods=['GET'])
def index():
    posts = [
        {
            'titulo': "Bienvenido a TRIVIA QUIZ",
            'texto': ""
        },
        {
            'titulo': "Objetivo: ",
            'texto': "El objetivo del juego es contestar correctamente una pregunta de cada una de las categorías propuestas, en el menor tiempo posible." + \
                     " Las categorías agrupan las preguntas de acuerdo a un tema."
        },
        {
            'titulo': "Reglas: ",
            'texto': "En el juego tendrá al menos éstas 4 categorías (pueden agregarse otras): - Historia - Arte - Geografía - " + \
                     "Deporte Cada categoría incluye varias preguntas. Cada una de las preguntas tiene asociadas tres posibles respuestas. " + \
                     "Sólo una de ellas es la correcta. El juego culmina cuando el jugador acierta una pregunta de cada categoría."
        },
        {
            'titulo': "Creador: ",
            'texto': "Fabio Suárez"
        },
        {
            'titulo': "Contacto: ",
            'texto': "defabiouy@yahoo.com"
        }
    ]

    trivia.inicializar_valores()

    return render_template('trivia.html', title='Home', posts=posts)


@app.route('/trivia/categorias',methods=['GET'])
def desplegar_categorias():

    try:
        retorno = []
        estados = []

        categorias_estado = session['dicc_categorias_estado']

        all_categories = Categoria.query.all()

        print(categorias_estado)
        for key1, valor in categorias_estado.items():
            elemento = {'key': str(key1),'valor': valor}
            estados.append(elemento)

        for categoria in all_categories:
            #print(categoria.id, categoria.nombre)
            elemento = {'key': str(categoria.id),'value': categoria.nombre}
            retorno.append(elemento)

        return render_template('categorias.html', title='Home', posts=retorno, estados=estados)
    except Exception as e:
        return render_template('error.html', title='Error', cod_error=500, mensaje=e.__doc__)


@app.route('/trivia/<int:nro_categoria>/pregunta',methods=['GET'])
def desplegar_pregunta(nro_categoria):

    try:
        respuestas = []
        categoria = Categoria.query.get(nro_categoria)

        cantidad_preg_categoria = db.session.query(Categoria).join(Categoria.preguntas).filter(Categoria.id==nro_categoria).count()

        #elijo la pregunta
        preg_aleatoria = randint(0,cantidad_preg_categoria-1)
        preguntas_de_la_categoria = []

        for preg in categoria.preguntas:
            preguntas_de_la_categoria.append(preg.id)
            print(preguntas_de_la_categoria)


        pregunta = Pregunta.query.get(preguntas_de_la_categoria[preg_aleatoria])

        pregunta_json = {'nro': str(pregunta.id),'texto': pregunta.texto}

        #recupero las posibles respuestas de la pregunta
        for respuesta in pregunta.respuestas:
            resp = {'key': str(respuesta.id),'value': respuesta.texto}
            respuestas.append(resp)
            print(respuestas)


        return render_template('pregunta.html', title='Home', pregunta=pregunta_json, respuestas=respuestas)
    except Exception as e:
        return render_template('error.html', title='Error', cod_error=500, mensaje=e.__doc__)


@app.route('/trivia/<int:nro_categoria>/<int:nro_pregunta>/resultado/<int:nro_respuesta>',methods=['GET'])
def desplegar_resultado(nro_categoria, nro_pregunta, nro_respuesta):

    try:
        resultado = ""
        restan_contestar = True
        #obtengo el diccionario de estados
        my_dicc_categorias_estado = session['dicc_categorias_estado']
        #print(nro_pregunta)
        #print(nro_respuesta)

        respuesta = Respuesta.query.get(nro_respuesta)
        print("respuesta", respuesta, respuesta.es_correcta)

        if respuesta.es_correcta=="True":
            resultado = 0 #"respuesta correcta"
            #actualizo el estado de la categoria
            print(my_dicc_categorias_estado)
            my_dicc_categorias_estado[str(nro_categoria)] = True
            session['dicc_categorias_estado'] = my_dicc_categorias_estado
            print(my_dicc_categorias_estado)
        else:
            resultado = 1 #"respuesta incorrecta"


        for estado in my_dicc_categorias_estado.values():
            if estado == False:
                restan_contestar = True
                break
            else:
                restan_contestar = False

        return render_template('resultado.html', title='Home', resultado=resultado, pendientes=restan_contestar)
    except Exception as e:
        return render_template('error.html', title='Error', cod_error=500, mensaje=e.__doc__)


@app.route('/trivia/fin',methods=['GET'])
def mostrar_saludo_final():

    try:
        minutos = trivia.contadorMinutos()
        trivia.inicializar_valores()

        return render_template('fin.html', title='FIN', resultado=minutos)
    except Exception as e:
        return render_template('error.html', title='Error', cod_error=500, mensaje=e.__doc__)