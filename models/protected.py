from routes.protected import api
from flask_restx import fields

#########
#REQUEST#
#########

model_protected_request = api.parser()

model_protected_request.add_argument("Authorization {token}", location="headers",type=str,help="token")

#########
#REPONSE#
#########

model_protected_response = api.model("Refresh_Response",{
    "IP":fields.String(description="ip do requisitante"),
})