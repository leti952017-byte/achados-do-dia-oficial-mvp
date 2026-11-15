from validacao import validar_produto


def test_produto_valido_nao_retorna_erros():
    assert validar_produto("Tênis", 99.90, "https://exemplo.com/p") == []


def test_preco_zero_gera_erro():
    erros = validar_produto("Tênis", 0, "https://exemplo.com/p")
    assert "Preço deve ser maior que zero." in erros


def test_link_sem_protocolo_gera_erro():
    erros = validar_produto("Tênis", 10, "exemplo.com")
    assert "Link de afiliado deve começar com http:// ou https://." in erros


def test_nome_vazio_gera_erro():
    erros = validar_produto("   ", 10, "https://exemplo.com")
    assert "Nome é obrigatório." in erros
