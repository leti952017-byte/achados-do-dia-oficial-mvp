def validar_produto(nome: str, preco: float, link_afiliado: str) -> list[str]:
    erros = []

    if not nome or not nome.strip():
        erros.append("Nome é obrigatório.")

    if preco is None or preco <= 0:
        erros.append("Preço deve ser maior que zero.")

    if not link_afiliado.startswith(("http://", "https://")):
        erros.append("Link de afiliado deve começar com http:// ou https://.")

    return erros
