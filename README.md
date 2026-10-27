## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/lucas-mendes1/studytrack-cli.git
cd studytrack-cli
```

### 2. Criar o ambiente virtual e instalar as dependências

**Windows (PowerShell):**

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
```

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

No Windows, os comandos utilizam diretamente o Python do ambiente virtual, sem exigir sua ativação pelo PowerShell.

### 3. Executar o programa

**Windows:**

```powershell
.\.venv\Scripts\python.exe -m studytrack
```

**Linux/macOS:**

```bash
python -m studytrack
```

Por padrão, os dados são armazenados em `~/.studytrack/sessions.json`.

Para utilizar outro caminho no Windows, defina a variável de ambiente antes de iniciar o programa:

```powershell
$env:STUDYTRACK_DATA = "$PWD\sessions.json"
.\.venv\Scripts\python.exe -m studytrack
```

### 4. Executar os testes

**Windows:**

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

**Linux/macOS:**

```bash
pytest -v
```

### 5. Verificar a qualidade do código

**Windows:**

```powershell
.\.venv\Scripts\ruff.exe check .
```

**Linux/macOS:**

```bash
ruff check .
```

## Gitflow adotado

- `main`: versão estável e pronta para entrega.
- `develop`: integração das funcionalidades em desenvolvimento.
- `feature/*`: desenvolvimento de novas funcionalidades a partir de `develop`.
- `release/*`: preparação e validação de uma versão.
- `hotfix/*`: correção urgente baseada em `main`.

O fluxo detalhado de comandos está em `docs/GITFLOW.md`.

## Escopo e melhorias futuras

Esta primeira versão é um MVP local. Possíveis evoluções: exportação CSV, interface web, API REST, banco de dados PostgreSQL e autenticação de usuários.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte `LICENSE`.
