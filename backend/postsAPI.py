# coding=utf-8
from flask_cors import CORS
from flask import Flask, request, jsonify, Response, render_template, abort
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import pyodbc
import json
from json import JSONEncoder



db_connect = create_engine('mssql+pyodbc://(localdb)\MSSQLLocalDB/Viajes?driver=SQL+Server+Native+Client+11.0?Trusted_Connection=yes', echo=True)
#db_connect = create_engine('sqlite:///chinook.db') #La ruta depende de donde tengas almacenada la base de datos
app = Flask(__name__)

@app.route('/test')
def mensaje():
    return jsonify('Nuevo mensaje desde servidor Flask')

# @app.route('/', defaults={'path':''})
# @app.route('/<path:path>')
# def render_vue(path):
#     return render_template('index.html')

api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

class Post():
    def __init__(self, codigo, titulo, fecha, descripcion, autor, dni):
        self.codigo = codigo
        self.titulo = titulo
        self.fecha = fecha.__str__()
        self.descripcion = descripcion
        self.autor = autor
        self.dni = dni


class Post_endpoint(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from posts join autores on posts.autor_dni = autores.dni")
        lista_posts = []

        for fila in query:
            post = Post(fila['id'],fila['titulo'], fila['fecha'], fila['descripcion'], fila['nombre'], fila['autor_dni'])
            lista_posts.append(post.__dict__)

        return jsonify(lista_posts)

    def post(self):
        conn = db_connect.connect()
        titulo = request.json['titulo']
        fecha = request.json['fecha']
        descripcion = request.json['descripcion']
        autor = request.json['autor']
        autor_dni = request.json['dni']
        fecha_nac = request.json['fecha_nac']

        query = conn.execute("select count(*) from autores where dni = {}".format(autor_dni))
        resultado = query.cursor.fetchone()[0]
        if resultado ==  0:
            conn.execute("insert into autores values('{0}','{1}','{2}')".format(autor_dni, autor, fecha_nac))

        query = conn.execute("insert into posts values('{0}','{1}','{2}','{3}')".format(titulo, fecha, descripcion, autor_dni))
        return {'status': 'Nuevo post añadido'}

    def delete(self):
        conn = db_connect.connect()
        codigo = request.args.get("codigo")
        query = conn.execute("select count(*) from posts where id = {}".format(codigo))
        resultado = query.cursor.fetchone()[0]
        if resultado ==  0:
            abort(400)

        query = conn.execute("delete from posts where id ={}".format(codigo))
       
        return {'status': 'Se a eliminado el Post'}



class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # Conexión a la Base de Datos
        query = conn.execute("select * from employees")  # Esta línea ejecuta un query y retorna un json como resultado
        return {'employees': [i[0] for i in query.cursor.fetchall()]}  # Se obtiene la primera columna que es EmployeeId

    def post(self):
        conn = db_connect.connect()
        last_name = request.json['LastName']
        first_name = request.json['FirstName']
        title = request.json['Title']
        reports_to = request.json['ReportsTo']
        birth_date = request.json['BirthDate']
        hire_date = request.json['HireDate']
        address = request.json['Address']
        city = request.json['City']
        state = request.json['State']
        country = request.json['Country']
        postal_code = request.json['PostalCode']
        phone = request.json['Phone']
        fax = request.json['Fax']
        email = request.json['Email']
        query = conn.execute("insert into employees values(null,'{0}','{1}','{2}','{3}', \
                             '{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}', \
                             '{13}')".format(last_name,first_name,title,
                                             reports_to, birth_date, hire_date, address,
                                             city, state, country, postal_code, phone, fax,
                                             email))
        return {'status': 'Nuevo empleado insertado'}


class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class EmployeeData(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d " % int(employee_id))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


api.add_resource(Employees, '/employees')  # Route_1
api.add_resource(Tracks, '/tracks')  # Route_2
api.add_resource(EmployeeData, '/employees/<employee_id>')  # Route_3
api.add_resource(Post_endpoint, '/api/posts')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port='5000', debug=True)