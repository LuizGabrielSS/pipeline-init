from routes.login import api
from flask_restx import fields

#########
#REQUEST#
#########

#Login#

model_login_request = api.parser()

model_login_request.add_argument("user",location="json",type=str,required=True,help="Usuario")

model_login_request.add_argument("password",location="json",type=str,help="Senha do usuario")

#Recarga#

model_refresh_request  = api.parser()

model_refresh_request.add_argument("Authorization {refresh}", location="headers",type=str,help="Refresh token")

#########
#REPONSE#
#########

model_refresh_response = api.model("Refresh_Response",{
    "Token":fields.String(description="Token para que utilize as outras rotas da api"),
    "Refresh_Token":fields.String(description="Refresh token para que possa atualizar a sua token e manter o seu acesso sem precisar logar novamente"),
})

model_login_response = api.model("Login_Response",{
    "Token":fields.String(description="Token para que utilize as outras rotas da api"),
    "Refresh_Token":fields.String(description="Refresh token para que possa atualizar a sua token e manter o seu acesso sem precisar logar novamente"),
})