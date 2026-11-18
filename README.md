# Docker Prática: Aplicação Flask

## Descrição
API simples em Flask, executada dentro de um contêiner Docker. Possui três rotas:

- `/` retorna uma mensagem de boas-vindas
- `/health` retorna o status da aplicação
- `/soma/<a>/<b>` retorna a soma de dois números inteiros

## Estrutura do projeto
```
docker-pratica/
├── app/
│   └── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Como construir a imagem
```bash
docker build -t minha-app .
```

## Como executar o contêiner
```bash
docker run -d --name minha-app -p 5000:5000 minha-app
```

A aplicação ficará disponível em http://localhost:5000

## Como verificar o funcionamento
- http://localhost:5000/ → `{"mensagem":"Olá, Docker!"}`
- http://localhost:5000/health → `{"status":"ok"}`
- http://localhost:5000/soma/2/3 → `{"resultado":5}`

## Como parar e remover o contêiner
```bash
docker rm -f minha-app
```