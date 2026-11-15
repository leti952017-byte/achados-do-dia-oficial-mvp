from app import create_app


def test_health_retorna_status_ok():
    app = create_app({"TESTING": True, "SECRET_KEY": "chave-de-teste"})
    client = app.test_client()

    resposta = client.get("/health")

    assert resposta.status_code == 200
    assert resposta.get_json() == {"status": "ok"}
