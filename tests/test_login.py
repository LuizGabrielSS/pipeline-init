#TESTES PARA A ROTA DE LOGIN#

def test_login(app,client):
    res = client.post('/login',json={
        "user":"teste",
        "password":"teste"
    })
    assert res.status_code == 200
    data = res.get_json()
    assert 'token' in data[0]
    assert 'refresh' in data[0]

def test_login_missing_body(app,client):
    res = client.post('/login',json={
        "user":"teste",
    })
    assert res.status_code == 500
