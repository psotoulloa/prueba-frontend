# -*- coding: utf-8 -*-
# Import librerías para Flask
from flask import Flask,render_template
from flask_restless import APIManager
# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Definimos la app
app = Flask(__name__)
# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

from sqlalchemy import Column,String,Integer,Text,Date

# Clase que representa una Tarea
class Tarea(db.Model):
	__tablename__ = "tareas"
	id= Column(Integer, primary_key=True)
	descripcion = Column(Text )
	fecha_comprometida = Column(Date,index=True)
	estado = Column(String(50),index=True)
	autor = Column(String(50), index=True)



@app.route("/")
def home():
	return "Nada aca"

#para manejar bug de no commit en flask restless
def commit_session(**kw):
	db.session.commit()

manager = APIManager(app, flask_sqlalchemy_db=db,
	preprocessors = dict(
		POST = [],
		GET_SINGLE = [],
		GET_MANY = [],
		PATCH_SINGLE = [],
		PATCH_MANY = [],
		DELETE_SINGLE = [],
		DELETE_MANY = []
	),
	postprocessors = dict(
        POST = [commit_session],
		PATCH_SINGLE = [commit_session],
		PATCH_MANY = [commit_session],
		DELETE_SINGLE = [commit_session],
		DELETE_MANY = [commit_session]
	))

def add_cors_headers(response):
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Credentials'] = 'true'
	response.headers['Access-Control-Allow-Headers'] = 'Apikey,Content-Type'

	response.headers['Access-Control-Allow-Methods'] = 'GET,POST,HEAD,OPTIONS,PUT,DELETE,PATCH'
	return response

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
blueprint1 = manager.create_api_blueprint(Tarea, methods=['GET', 'PATCH', 'POST', 'DELETE', 'OPTIONS'])

blueprint1.after_request(add_cors_headers)

app.register_blueprint(blueprint1)

@app.teardown_appcontext
def shutdown_session ( exception=None ):
	db.session.commit()
	db.session.close()
	print("Commiting")


if __name__ == "__main__":
	app.run(host="0.0.0.0",port=5000)


