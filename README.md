
# API Containerizada

API REST desenvolvida com FastAPI, PostgreSQL e Docker, com autenticação de usuários e gerenciamento de tarefas.

O projeto foi desenvolvido para praticar a construção de APIs backend em Python, integração com banco de dados relacional, containerização e deploy em ambiente de produção.

## Tecnologias utilizadas

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose
- JWT
- Pydantic
- Uvicorn
- Render

## Funcionalidades

- Cadastro de usuários.
- Autenticação com JWT.
- Login de usuários.
- Criação de tarefas.
- Consulta de tarefas.
- Atualização de tarefas.
- Exclusão de tarefas.
- Integração com PostgreSQL.
- Execução local com Docker Compose.
- Deploy da API no Render.

## Arquitetura do projeto

```text
api_containerizada/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   ├── usuarios.py
│   │   └── tarefas.py
│   │
│   └── ...
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── .env.example
├── .dockerignore
├── .gitignore
└── README.md
```

> A estrutura acima é um exemplo. Ajuste os nomes das pastas e arquivos para corresponder exatamente à estrutura atual do projeto.

## Como executar localmente

### Pré-requisitos

- Python 3.12 ou superior.
- Docker Desktop.
- Git.

### 1. Clonar o repositório

```bash
git clone https://github.com/marcos16744/api_containerizada.git
```

```bash
cd api_containerizada
```

### 2. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto.

Exemplo:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=api_containerizada

SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Utilize valores próprios para as variáveis e não compartilhe senhas reais.

### 3. Executar com Docker Compose

```bash
docker compose up --build
```

O Docker irá construir a imagem da API, instalar as dependências e iniciar os serviços definidos no Docker Compose.

### 4. Acessar a API

Após a inicialização:

```text
http://localhost:8000
```

Documentação interativa:

```text
http://localhost:8000/docs
```

## Banco de dados

O projeto utiliza PostgreSQL como banco de dados relacional.

A comunicação com o banco é realizada por meio do SQLAlchemy.

A configuração do banco utiliza variáveis de ambiente para evitar que credenciais fiquem diretamente no código.

Localmente, a aplicação utiliza o PostgreSQL configurado no Docker Compose.

Em produção, a API utiliza o PostgreSQL hospedado no Render por meio da variável `DATABASE_URL`.

## Deploy

A API foi publicada utilizando o Render.

### Configuração de produção

- API hospedada em um Web Service.
- Banco PostgreSQL gerenciado pelo Render.
- Variáveis de ambiente configuradas no painel do Render.
- Conexão com o banco utilizando `DATABASE_URL`.
- Comando de inicialização com Uvicorn.

### Comando de inicialização

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

> Ajuste o caminho `app.main:app` caso o arquivo `main.py` esteja em outra localização.

### Link do deploy

Adicione aqui a URL pública da sua API:

```text
https://SEU-ENDERECO.onrender.com
```

Documentação Swagger:

```text
https://SEU-ENDERECO.onrender.com/docs
```

## Segurança

- As credenciais do banco não são armazenadas no GitHub.
- O arquivo `.env` está incluído no `.gitignore`.
- As variáveis de ambiente são configuradas separadamente no Render.
- A chave secreta do JWT deve ser mantida em segredo.
- O projeto utiliza autenticação para proteger endpoints privados.

## Objetivos de aprendizado

Este projeto foi desenvolvido para praticar:

- Desenvolvimento de APIs REST com FastAPI.
- Organização de projetos backend em Python.
- Integração com PostgreSQL.
- ORM com SQLAlchemy.
- Autenticação utilizando JWT.
- Containerização com Docker.
- Orquestração com Docker Compose.
- Variáveis de ambiente.
- Deploy de aplicações backend.
- Persistência de dados em produção.

## Próximos passos

- Adicionar testes automatizados com pytest.
- Implementar logging estruturado.
- Melhorar o tratamento de erros.
- Adicionar novas funcionalidades à API.
- Evoluir a arquitetura do projeto.

## Autor

Marcos Vinicius

GitHub: https://github.com/marcos16744
