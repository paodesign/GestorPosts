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

class Post():#se crea la clase post
    def __init__(self, codigo, titulo, fecha, descripcion, autor, dni): #definimos sus atributos
        self.codigo = codigo
        self.titulo = titulo
        self.fecha = fecha.__str__()
        self.descripcion = descripcion
        self.autor = autor
        self.dni = dni


class Post_endpoint(Resource): #se crea una clase donde se definiran los endpoint
    @app.route('/api/posts')
    def getAll():# endpoint GET obtiene los post y los envia como objetos en un array "lista_post"
        conn = db_connect.connect() # se guarda la conexión a base de datos
        query = conn.execute("select * from posts join autores on posts.autor_dni = autores.dni")# se ejecuta la conexión a base de datos y se consulta(obtenga de las tablas posts y la tabla autores,el dni que sea igual en ambas tablas)
        lista_posts = [] #se decalra un array vasió 

        for fila in query:
            post = Post(fila['id'],fila['titulo'], fila['fecha'], fila['descripcion'], fila['nombre'], fila['autor_dni'])
            lista_posts.append(post.__dict__) #se agrega post al array

        return jsonify(lista_posts)#retorna la respueta en forma de objeto

    def post(self): #endpoint POST crea el post
        conn = db_connect.connect()# se guarda en una variable la conexión a basa de datos
        titulo = request.json['titulo']# se  realiza la petición http, se busca la clave para obtener su valor y se lo guarda en una variable
        fecha = request.json['fecha']
        descripcion = request.json['descripcion']
        autor = request.json['autor']
        autor_dni = request.json['dni']
        fecha_nac = request.json['fecha_nac']

        query = conn.execute("select count(*) from autores where dni = {}".format(autor_dni))# se ejecuta la conexión a base de datos,y se realiza la consulta(queremos saber la cant, de autores con el mismo dni)
        resultado = query.cursor.fetchone()[0] #se guaraga el resultado obtenido en la consulta
        if resultado ==  0:# si el resultado es igual a cero se crea un nuevo autor
            conn.execute("insert into autores values('{0}','{1}','{2}')".format(autor_dni, autor, fecha_nac))#se ejecuta la conexión, se añade datos a la tabla creando el autor

        query = conn.execute("insert into posts values('{0}','{1}','{2}','{3}')".format(titulo, fecha, descripcion, autor_dni))#se ejecuta la conexión a base de datos,y se agrega datos a la tabla posts creando un nuevo posts
        return {'status': 'Nuevo post añadido'}# returna el estado de nuestar petición

    def delete(self):# endpoint DELETE elimina el post
        conn = db_connect.connect()# se guarda la conexión a base de datos
        codigo = request.args.get("codigo")# se realiza la petición http, que obtenga el código unívoco
        query = conn.execute("select count(*) from posts where id = {}".format(codigo))# se ejecuta la conexión y se realiza la consulta(queremos saber cuantos posts tiene ese id o código unívoco)
        resultado = query.cursor.fetchone()[0]# se guarga el resultado obtenido en la consulta
        if resultado ==  0: #si el resultado es igual a cero
            abort(400) #se manda error, no se puede realizar esa petición, no existe

        query = conn.execute("delete from posts where id ={}".format(codigo))# se ejecuta la conexión a la base de datos y se elimina ese post.
       
        return {'status': 'Se a eliminado el Post'}# retorna el estado 

    def put(self): #endpoint PUT editar un post ya existente
        conn = db_connect.connect()# se guarda la conexión a la basa de datos
        codigo = request.args.get("codigo")# se realiza la petición http, que obtenga el código unívoco
        titulo = request.json['titulo']# se  realiza la petición http, se busca la clave para obtener su valor y se lo guarda en una variable
        descripcion = request.json['descripcion']

        query = conn.execute("update posts set titulo = '{0}', descripcion = '{1}' where id = '{2}'".format(titulo, descripcion, codigo))#se ejecuta la conexión a base de datos y se módifican los datos del post
        return {'status': 'Se a modificado el Post'}

<<<<<<< HEAD
    def get(self, id):
        conn = db_connect.connect()
        codigo = request.args.get("codigo")
        query = conn.execute("") 




class Employees(Resource):
    def get(self):# se crea una función recibir
        conn = db_connect.connect() # Conexión a la Base de Datos
        query = conn.execute("select * from employees")  # Esta línea ejecuta un query y retorna un json como resultado
        return {'employees': [i[0] for i in query.cursor.fetchall()]}  # Se obtiene la primera columna que es EmployeeId

    def post(self):# se crea una función modificar
        conn = db_connect.connect()# Conexión a la Base de Datos
        last_name = request.json['LastName'] #guargamos en esta variable 
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
=======
    @app.route('/api/posts/<int:codigo>', methods=['GET'])
    def getById(codigo):
>>>>>>> fd5f9bb941f521a1a71a2d7824da3f4f5707e4f5
        conn = db_connect.connect()
        query = conn.execute("select p.id, p.titulo, p.fecha, p.descripcion, a.nombre, a.dni from posts p join autores a on p.autor_dni = a.dni where id = '{}'".format(codigo))
        fila = query.cursor.fetchall()[0]
        post = Post(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])

        return jsonify(post.__dict__)
    
class Autor():
    def __init__(self, dni, nombre, fecha_nac):
        self.dni = dni
        self.nombre = nombre
        self.fecha_nac = fecha_nac.__str__()


class Autor_endpoint(Resource):
    def get(dni):
        conn = db_connect.connect()
        query = conn.execute("select * from autores")
        lista_autores= []
        for fila in query:
            autor = Autor(fila['dni'],fila['nombre'], fila['fecha_nac'])
            lista_autores.append(autor.__dict__)

        return jsonify(lista_autores)


api.add_resource(Post_endpoint, '/api/posts')
api.add_resource(Autor_endpoint, '/api/autores')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port='5000', debug=True)