from app import db


class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False, unique=True)
    preguntas = db.relationship('Pregunta', backref='categoria', lazy='dynamic')

    def __str__(self):
        return '<Categoria %s>' % self.name


class Pregunta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(255), nullable=False, unique=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    respuestas = db.relationship('Respuesta', backref='pregunta', lazy='dynamic')

    def __str__(self):
        return '<Pregunta %s>' % self.text


class Respuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(255), nullable=False, unique=False)
    es_correcta = db.Column(db.String(5), nullable=False, unique=False)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('pregunta.id'))

    def __str__(self):
        return '<Respuesta %s>' % self.texto
