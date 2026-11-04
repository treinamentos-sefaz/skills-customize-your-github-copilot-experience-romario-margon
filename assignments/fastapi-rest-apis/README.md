# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objetivo

Crie uma API REST para cadastrar e consultar livros usando FastAPI. Você praticará rotas HTTP, validação de dados com Pydantic e respostas com códigos de status apropriados.

## 📝 Tarefas

### 🛠️ Configure a Aplicação e Consulte Livros

#### Descrição
Instale as dependências com `python -m pip install fastapi uvicorn` e inicie a aplicação com `uvicorn starter-code:app --reload`. Depois, implemente rotas para listar os livros cadastrados e consultar um livro pelo seu identificador.

#### Requisitos
O programa concluído deve:

- Usar os modelos `BookInput` e `Book` para validar os dados e representar livros.
- Implementar `GET /books` para retornar a lista de livros.
- Implementar `GET /books/{book_id}` para retornar um livro específico.
- Responder com status HTTP 404 quando o identificador solicitado não existir.

### 🛠️ Cadastre, Atualize e Remova Livros

#### Descrição
Implemente as rotas restantes para criar, atualizar e remover livros do catálogo em memória.

#### Requisitos
O programa concluído deve:

- Implementar `POST /books` para cadastrar um livro e retornar o registro criado com status HTTP 201.
- Implementar `PUT /books/{book_id}` para atualizar o título e o autor de um livro existente.
- Implementar `DELETE /books/{book_id}` para remover um livro existente.
- Responder com status HTTP 404 ao tentar atualizar ou remover um livro inexistente.
- Permitir testar e consultar as rotas pela documentação interativa disponível em `/docs`.
