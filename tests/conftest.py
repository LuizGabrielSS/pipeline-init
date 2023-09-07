import pytest
from app import create_app as flask_app
import jwt
import datetime

@pytest.fixture()
def app():
    app = flask_app()
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner():
    # Use o token JWT gerado nos seus testes
    secret_key = "Senha secreta da api"  # A mesma chave usada na configuração do Flask-JWT-Extended
    experies = datetime.timedelta(seconds=1)  # Prazo de validade do token

    payload = {
        'sub': 'user_id',  # Identificação do usuário
        'exp': datetime.datetime.utcnow() + experies
    }

    token = jwt.encode(payload, secret_key, algorithm='HS256')

    headers = {'Authorization': f'Bearer {token}'}

    return headers