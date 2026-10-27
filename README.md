# StudyTrack CLI

[![CI - StudyTrack](https://github.com/lucas-mendes1/studytrack-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/lucas-mendes1/studytrack-cli/actions/workflows/ci.yml)

Aplicação de linha de comando para registrar sessões de estudo, consultar o histórico e acompanhar o tempo dedicado a cada disciplina. O projeto foi desenvolvido como prática de Python, testes automatizados, Gitflow e integração contínua com GitHub Actions.

## Funcionalidades

- Registrar uma sessão com disciplina, data, duração e conteúdo estudado.
- Listar as sessões salvas.
- Consultar o tempo total e a distribuição de minutos por disciplina.
- Validar disciplina, data e duração.
- Armazenar os dados localmente em JSON.
- Executar testes automatizados e análise estática na pipeline de CI.

## Tecnologias

- Python 3.11 ou superior
- Pytest — testes automatizados
- Ruff — análise estática e qualidade do código
- Git e GitHub — versionamento
- GitHub Actions — integração contínua

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/lucas-mendes1/studytrack-cli.git
cd studytrack-cli
```

### 2. Criar e ativar um ambiente virtual

Windows (PowerShell):

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências de desenvolvimento

```bash
python -m pip install -e ".[dev]"
```

### 4. Iniciar o programa

```bash
python -m studytrack
```

Por padrão, os dados são guardados em `~/.studytrack/sessions.json`. Para usar outro caminho, defina a variável de ambiente `STUDYTRACK_DATA` antes de iniciar o programa.

PowerShell:

```powershell
$env:STUDYTRACK_DATA = "$PWD\sessions.json"
python -m studytrack
```

## Como executar os testes

```bash
pytest -v
```

## Como executar a análise estática

```bash
ruff check .
```

## Gitflow adotado

- `main`: versão estável e pronta para entrega.
- `develop`: integração das funcionalidades em desenvolvimento.
- `feature/*`: desenvolvimento de novas funcionalidades a partir de `develop`.
- `release/*`: preparação e validação de uma versão.
- `hotfix/*`: correção urgente baseada em `main`.

O fluxo detalhado de comandos está em [`docs/GITFLOW.md`](docs/GITFLOW.md).

## Escopo e melhorias futuras

Esta primeira versão é um MVP local. Possíveis evoluções: exportação CSV, interface web, API REST, banco de dados PostgreSQL e autenticação de usuários.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte [`LICENSE`](LICENSE).
