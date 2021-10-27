
from flask import Flask, send_from_directory

#from flask.signals import appcontext_popped
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
#flask.scaffold is added for cateringto errors in flask cors
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
# from api.HelloApiHandler import HelloApiHandler

# import HelloApiHandler

# something wrong with hello api handler

print("yo")
app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app)

api = Api(app)

@app.route("/")
def index(path):
    print("hello")
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

# api.add_resource(HelloApiHandler, '/flask/hello')
