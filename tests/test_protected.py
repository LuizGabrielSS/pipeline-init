def test_rota_protegida_com_jwt(client,runner):
    
    response = client.post('/protected', headers=runner)

    assert response.status_code == 200  # Substitua 200 pelo código de status esperado