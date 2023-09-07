#Flask
from flask import Flask,Blueprint
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_restx import Api

from private.secret_key import Secret_Key

from private.endereco_api import host_api,porta_api

from routes.login import api as login

from routes.protected import api as protected

def create_app(Teste=False):

    app = Flask(__name__)

    app.config["JWT_SECRET_KEY"] = Secret_Key

    app.config.TESTING = Teste

    main_route = Blueprint('api', __name__)

    api = Api(main_route,
        title='Api Segfis Mobile',
        description='Swagger da api do segfis mobile',
        version='2.0',
        doc='/Doc'
        )

    api.add_namespace(login)

    api.add_namespace(protected)

    app.register_blueprint(main_route)

    JWTManager(app)

    CORS(app)

    return app

if __name__ == '__main__':

    app = create_app()

    app.run(
        host_api,
        porta_api,
        debug=True,
        threaded=True
        )