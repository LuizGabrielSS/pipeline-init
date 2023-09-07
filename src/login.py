import json
from flask_jwt_extended import create_access_token,create_refresh_token,get_jwt_identity
import datetime

def Login(User,Passwoard):

    #Lembre-se de definir o tempo da token e da refresh, elas nao podem ser eternas

    experies = datetime.timedelta(minutes=10)

    experies_refresh = datetime.timedelta(minutes=60)

    access_token = create_access_token(identity=User,expires_delta=experies)

    refresh_token = create_refresh_token(identity=User,expires_delta=experies_refresh)

    j = json.dumps(
        [
            {
                "token":access_token,
                "refresh":refresh_token
            }
        ]
    )

    j = json.loads(j)

    return j

def Recarga():

    identify = get_jwt_identity()

    experies = datetime.timedelta(minutes=10)

    experies_refresh = datetime.timedelta(minutes=60)
    
    access_token = create_access_token(identity=identify,expires_delta=experies)
    
    refresh_token = create_refresh_token(identity=identify,expires_delta=experies_refresh)

    j = json.dumps(
        [
            {
                "Token":access_token,
                "Refresh_Token":refresh_token
            }
        ]
    )

    j = json.loads(j)

    return j