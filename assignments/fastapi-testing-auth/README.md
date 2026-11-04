# 📘 Assignment: API Testing and Authentication

## 🎯 Objetivo

Amplie uma API FastAPI com testes automatizados e autenticação por chave de API, verificando respostas corretas para solicitações autorizadas e não autorizadas.

## 📝 Tarefas

### 🛠️ Teste uma Rota com pytest

#### Descrição
Instale as dependências com `python -m pip install fastapi pytest httpx` e execute os testes do código inicial com `python -m pytest assignments/fastapi-testing-auth/starter-code.py`. Use o `TestClient` para verificar o comportamento da rota sem iniciar um servidor.

#### Requisitos
O programa concluído deve:

- Manter o teste de `GET /books` verificando o status HTTP 200.
- Verificar que a resposta é uma lista de livros com identificador, título e autor.
- Adicionar pelo menos um teste para um comportamento da API além do caso já demonstrado.

### 🛠️ Proteja a Criação de Livros

#### Descrição
Proteja `POST /books` usando uma chave enviada no cabeçalho `X-API-Key`. A chave de demonstração no código serve apenas para este exercício e não deve ser usada em produção.

#### Requisitos
O programa concluído deve:

- Usar `APIKeyHeader` e uma dependência do FastAPI para ler e validar a chave.
- Retornar status HTTP 401 quando a chave estiver ausente ou incorreta.
- Criar e retornar o livro com status HTTP 201 quando a chave estiver correta.

### 🛠️ Teste os Cenários de Autenticação

#### Descrição
Complete a suíte de testes para confirmar que a rota protegida aceita somente solicitações com a chave correta.

#### Requisitos
O programa concluído deve:

- Testar uma criação autorizada e verificar status 201 e os dados do livro criado.
- Testar solicitações sem chave e com chave incorreta, verificando status 401.
- Executar os testes com `python -m pytest assignments/fastapi-testing-auth/starter-code.py` e confirmar que todos passam.
