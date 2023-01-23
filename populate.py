#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app import db
from app.models import Categoria, Pregunta, Respuesta

db.drop_all()
db.create_all()

#categorias
c_historia = Categoria(nombre="Historia")
c_geogra = Categoria(nombre="Geografía")
c_deporte = Categoria(nombre="Deportes")
c_arte = Categoria(nombre="Arte")

#preguntas categoria historia --------------------------------------------------
p_descAmerica = Pregunta(texto="¿En que año se descubrio américa?", categoria=c_historia)
p_orientales = Pregunta(texto="¿Cuantos eran los 33 orientales?", categoria=c_historia)
p_napoleon = Pregunta(texto="¿Donde nació Napoleon?", categoria=c_historia)

#respuestas categoria historia
r_descAmerica1 = Respuesta(texto="1492", es_correcta="True", pregunta=p_descAmerica)
r_descAmerica2 = Respuesta(texto="1515", es_correcta="False", pregunta=p_descAmerica)
r_descAmerica3 = Respuesta(texto="1980", es_correcta="False", pregunta=p_descAmerica)

r_orientales1 = Respuesta(texto="33", es_correcta="False", pregunta=p_orientales)
r_orientales2 = Respuesta(texto="menos de 33", es_correcta="False", pregunta=p_orientales)
r_orientales3 = Respuesta(texto="mas de 33", es_correcta="True", pregunta=p_orientales)

r_napoleon1 = Respuesta(texto="Inglaterra", es_correcta="False", pregunta=p_napoleon)
r_napoleon2 = Respuesta(texto="Francia", es_correcta="True", pregunta=p_napoleon)
r_napoleon3 = Respuesta(texto="España", es_correcta="False", pregunta=p_napoleon)


#preguntas categoria geografia --------------------------------------------------
p_amazonas = Pregunta(texto="¿En que continente esta el Amazonas?", categoria=c_geogra)
p_montania = Pregunta(texto="¿Cual es la montaña mas alta del mundo?", categoria=c_geogra)
p_pais = Pregunta(texto="¿Que país es el 2do mas grande del mundo en términos de población?", categoria=c_geogra)

#respuestas categoria geografia
r_amazonas1 = Respuesta(texto="Europa", es_correcta="False", pregunta=p_amazonas)
r_amazonas2 = Respuesta(texto="Africa", es_correcta="False", pregunta=p_amazonas)
r_amazonas3 = Respuesta(texto="América", es_correcta="True", pregunta=p_amazonas)

r_montania1 = Respuesta(texto="Cerro chato", es_correcta="False", pregunta=p_montania)
r_montania2 = Respuesta(texto="El everest", es_correcta="True", pregunta=p_montania)
r_montania3 = Respuesta(texto="El Aconcagua", es_correcta="False", pregunta=p_montania)

r_pais1 = Respuesta(texto="India", es_correcta="True", pregunta=p_pais)
r_pais2 = Respuesta(texto="China", es_correcta="False", pregunta=p_pais)
r_pais3 = Respuesta(texto="Rusia", es_correcta="False", pregunta=p_pais)


#preguntas categoria deporte --------------------------------------------------
p_uyCampeon = Pregunta(texto="¿Uruguay va a salir campeon de América?", categoria=c_deporte)
p_tyson = Pregunta(texto="¿Tyson sigue boxeando?", categoria=c_deporte)
p_copas = Pregunta(texto="¿Cuantas copas americas tiene uruguay?", categoria=c_deporte)

#respuestas categoria deporte
r_uyCampeon1 = Respuesta(texto="Quizas", es_correcta="True", pregunta=p_uyCampeon)
r_uyCampeon2 = Respuesta(texto="No", es_correcta="False", pregunta=p_uyCampeon)
r_uyCampeon3 = Respuesta(texto="Si", es_correcta="False", pregunta=p_uyCampeon)

r_tyson1 = Respuesta(texto="No, solo muerde", es_correcta="False", pregunta=p_tyson)
r_tyson2 = Respuesta(texto="Obviamente", es_correcta="False", pregunta=p_tyson)
r_tyson3 = Respuesta(texto="Ahora solo actua", es_correcta="True", pregunta=p_tyson)

r_copas1 = Respuesta(texto="14", es_correcta="False", pregunta=p_copas)
r_copas2 = Respuesta(texto="15", es_correcta="True", pregunta=p_copas)
r_copas3 = Respuesta(texto="16", es_correcta="False", pregunta=p_copas)


#preguntas categoria arte --------------------------------------------------
p_picasso = Pregunta(texto="¿Picasso es el padre del cubismo?", categoria=c_arte)
p_sixtina = Pregunta(texto="¿Quien pintó la capilla sixtina?", categoria=c_arte)
p_coliseo = Pregunta(texto="¿Que estilo tienen las columnas inferiores del Coliseo?", categoria=c_arte)

#respuestas categoria arte
r_picasso1 = Respuesta(texto="No se", es_correcta="False", pregunta=p_picasso)
r_picasso2 = Respuesta(texto="No", es_correcta="False", pregunta=p_picasso)
r_picasso3 = Respuesta(texto="Si", es_correcta="True", pregunta=p_picasso)

r_sixtina1 = Respuesta(texto="Rafael", es_correcta="False", pregunta=p_sixtina)
r_sixtina2 = Respuesta(texto="Donatello", es_correcta="False", pregunta=p_sixtina)
r_sixtina3 = Respuesta(texto="Miguel Angel", es_correcta="True", pregunta=p_sixtina)

r_coliseo1 = Respuesta(texto="Dorico", es_correcta="True", pregunta=p_coliseo)
r_coliseo2 = Respuesta(texto="Jonico", es_correcta="False", pregunta=p_coliseo)
r_coliseo3 = Respuesta(texto="Corintio", es_correcta="False", pregunta=p_coliseo)


# agregamos todo a la sesión y luego commmiteamos
#categorias
db.session.add(c_historia)
db.session.add(c_geogra)
db.session.add(c_deporte)
db.session.add(c_arte)

#preguntas categoria historia --------------------------------------------------
db.session.add(p_descAmerica)
db.session.add(p_orientales)
db.session.add(p_napoleon)

#respuestas categoria historia
db.session.add(r_descAmerica1)
db.session.add(r_orientales1)
db.session.add(r_napoleon1)

db.session.add(r_descAmerica2)
db.session.add(r_orientales2)
db.session.add(r_napoleon2)

db.session.add(r_descAmerica3)
db.session.add(r_orientales3)
db.session.add(r_napoleon3)

#preguntas categoria geografia --------------------------------------------------
db.session.add(p_amazonas)
db.session.add(p_montania)
db.session.add(p_pais)

#respuestas categoria geografia
db.session.add(r_amazonas1)
db.session.add(r_montania1)
db.session.add(r_pais1)

db.session.add(r_amazonas2)
db.session.add(r_montania2)
db.session.add(r_pais2)

db.session.add(r_amazonas3)
db.session.add(r_montania3)
db.session.add(r_pais3)

#preguntas categoria deporte --------------------------------------------------
db.session.add(p_uyCampeon)
db.session.add(p_tyson)
db.session.add(p_copas)

#respuestas categoria deporte
db.session.add(r_uyCampeon1)
db.session.add(r_tyson1)
db.session.add(r_copas1)

db.session.add(r_uyCampeon2)
db.session.add(r_tyson2)
db.session.add(r_copas2)

db.session.add(r_uyCampeon3)
db.session.add(r_tyson3)
db.session.add(r_copas3)

#preguntas categoria arte --------------------------------------------------
db.session.add(p_picasso)
db.session.add(p_sixtina)
db.session.add(p_coliseo)

#respuestas categoria arte
db.session.add(r_picasso1)
db.session.add(r_sixtina1)
db.session.add(r_coliseo1)

db.session.add(r_picasso2)
db.session.add(r_sixtina2)
db.session.add(r_coliseo2)

db.session.add(r_picasso3)
db.session.add(r_sixtina3)
db.session.add(r_coliseo3)

db.session.commit()