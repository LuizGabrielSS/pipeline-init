#Flask
from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace,Resource

from src.login import Login,Recarga

api = Namespace("login","Rotas relacionadas ao login")

from models.login import model_login_response,model_login_request,model_refresh_response,model_refresh_request

@api.route("")
class Logins(Resource):
    @api.response(200,'Sucesso',model_login_response)
    @api.expect(model_login_request)
    def post(self):
        Dados = request.get_json()
        User = Dados['user']
        Password = Dados['password']
        return Login(User,Password)

@api.route("/refresh")
class Recarregando(Resource):
    @api.response(209,'Sucesso',model_refresh_response)
    @api.expect(model_refresh_request)
    @jwt_required(refresh=True)
    def post(self):
        return Recarga()