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

## Integração contínua (GitHub Actions)

O workflow `.github/workflows/ci.yml` executa em **pushes na branch `main`** e em **Pull Requests**. Ele faz o seguinte:

1. Constrói a imagem Docker
2. Inicia um contêiner com a aplicação
3. Aguarda a aplicação responder
4. Executa os testes automatizados (`pytest`) contra o contêiner

Se algum teste falhar, o workflow falha.

## O que foi testado

Os testes estão em `tests/test_app.py` e fazem requisições HTTP à aplicação rodando no contêiner:

- `test_home`: a rota `/` retorna status 200 e a mensagem "Olá, Docker!"
- `test_health`: a rota `/health` retorna status 200 e `status: ok`
- `test_soma`: a rota `/soma/2/3` retorna status 200 e `resultado: 5`

## Erro proposital e correção

**Alteração feita:** na rota `/soma` do arquivo `app/app.py`, troquei `a + b` por `a - b`.

**Causa da falha:** o teste `test_soma` esperava o resultado 5 (2 + 3), mas a aplicação retornou -1 (2 - 3), gerando `assert -1 == 5`. Como o teste falhou, o passo "Executar testes" terminou com erro e o workflow ficou vermelho.

**Correção:** voltei a operação para `a + b`, sem alterar os testes.

**Links das execuções:**

- Execução com erro: https://github.com/KamilaPacifico/docker-pratica/actions/runs/44220396935/job/134520515681
- Execução após a correção: https://github.com/KamilaPacifico/docker-pratica/actions/runs/44221692440/job/134524859729