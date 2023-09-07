#Flask
from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace,Resource

from src.protected import protect

api = Namespace("protected","Rotas protegidas pela token")

from models.protected import model_protected_request,model_protected_response

@api.route("")
class Protected(Resource):
    @api.response(200,'Sucesso',model_protected_response)
    @api.expect(model_protected_request)
    def post(self):
        return protect()