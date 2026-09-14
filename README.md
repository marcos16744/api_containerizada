# API Containerizada

Projeto de estudo desenvolvido para aprender a containerização de uma aplicação FastAPI utilizando Docker e Docker Compose.

## Tecnologias

* Python
* FastAPI
* Uvicorn
* Docker
* Docker Compose
* PostgreSQL

## Conceitos praticados

* Criação de imagens com Dockerfile.
* Execução de containers.
* Orquestração de serviços com Docker Compose.
* Variáveis de ambiente com `.env`.
* Comunicação entre containers.
* Configuração de portas e serviços.

## Como executar

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
cd api-containerizada
```

Crie um arquivo `.env` com as variáveis necessárias e execute:

```bash
docker compose up --build
```

A API estará disponível em:

```text
http://localhost:8000
```

Documentação Swagger:

```text
http://localhost:8000/docs
```

## Objetivo

Consolidar conhecimentos de Docker e preparar uma aplicação Python para execução em ambientes isolados e reproduzíveis.
