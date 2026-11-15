# Achados do Dia Oficial

Catálogo público e gratuito de ofertas de afiliados (Amazon e Mercado Livre) do **Achados do Dia Oficial**, pequeno empreendimento de marketing digital e afiliação do ABC Paulista.

> Projeto desenvolvido na disciplina Projeto de Software – Experiência Prática 2, do curso de Análise e Desenvolvimento de Sistemas (EaD), por Letícia Silva Cruz.

## Problema

A administradora divulga produtos apenas por WhatsApp e Instagram. Toda a rotina (selecionar ofertas, organizar links, atualizar preços e reenviar informações) é manual. Além disso:

- os links se perdem entre publicações antigas;
- não existe um lugar onde o consumidor pesquise ofertas já divulgadas;
- não há registro de cliques, então não se sabe quais produtos despertam interesse.

## Solução

Um catálogo web em que a administradora cadastra produtos com link de afiliado e o consumidor navega, pesquisa e acessa a loja parceira.

### Requisitos funcionais

|
 Código 
|
 Requisito 
|
 Prioridade 
|
|
---
|
---
|
---
|
|
 RF01 
|
 Cadastro de produto pela administradora autenticada, com validação 
|
 Obrigatório 
|
|
 RF02 
|
 Vitrine pública agrupada por categoria 
|
 Obrigatório 
|
|
 RF03 
|
 Busca de produtos por nome 
|
 Obrigatório 
|
|
 RF04 
|
 Registro de clique e redirecionamento ao link de afiliado 
|
 Obrigatório 
|
|
 RF05 
|
 Edição e despublicação de produto, sem exclusão física 
|
 Desejável 
|
|
 RF06 
|
 Painel de cliques por produto, ordenável 
|
 Desejável 
|

Fora do escopo: pagamentos, carrinho, entregas e aplicativo nativo.

## Público-alvo

- **Usuária direta:** a administradora do empreendimento, que cadastra produtos e acompanha cliques.
- **Consumidores:** pessoas que acessam o site pelo celular, muitas vezes em conexão limitada.
- **Beneficiados indiretos:** pequenos comerciantes, empreendedores digitais e a comunidade do ABC Paulista.

## Tecnologias

- Python 3.12
- Flask 3.0 (roteamento e regras de negócio)
- Jinja2 3.1 (renderização das telas)
- Werkzeug 3.0 (validação e hash de senha)
- Flask-Login 0.6 (autenticação da administradora)
- Supabase (PostgreSQL gerenciado) com cliente oficial para Python
- pytest (testes automatizados)
- Gunicorn (servidor de produção)
- Hospedagem: Render

## Arquitetura

Monolito em três camadas:

1. **Apresentação:** HTML, CSS e Jinja2. Exibe e captura dados.
2. **Lógica de aplicação:** Flask. Valida entradas, aplica regras e trata respostas.
3. **Persistência:** Supabase. Guarda produtos, categorias e registros de cliques.

## Como executar localmente

> Os arquivos citados abaixo serão adicionados ao longo do desenvolvimento.

1. Clone o repositório:
   `git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git`
2. Crie e ative um ambiente virtual:
   `python -m venv .venv` e depois `.venv\Scripts\activate` (Windows) ou `source .venv/bin/activate` (Linux/macOS)
3. Instale as dependências:
   `pip install -r requirements.txt`
4. Copie `.env.example` para `.env` e preencha as variáveis:
   - `SUPABASE_URL`
   - `SUPABASE_ANON_KEY`
   - `SECRET_KEY`
   - `FLASK_ENV=development`
5. Execute a aplicação:
   `flask --app app run`
6. Execute os testes:
   `pytest`

## Testes e Integração Contínua

Os testes unitários e de integração são executados com pytest. O GitHub Actions roda os testes a cada push e a cada Pull Request.

## Fluxo de contribuição

- Cada funcionalidade é desenvolvida em uma branch (ex.: `feat/cadastro-produto`).
- As alterações entram na `principal` por meio de Pull Request, somente com o CI aprovado.
- As mensagens de commit seguem o padrão `feat`, `fix`, `docs`, `test` e `ci`.

## Documentação complementar

- `docs/validacao/`: registro das rodadas de validação com a parceira.
- `docs/desempenho/`: registro das medições de desempenho (RNF03).
