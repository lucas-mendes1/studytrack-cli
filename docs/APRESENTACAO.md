# Roteiro de apresentação — StudyTrack CLI

## Demonstração funcional (1–2 minutos)

1. Abra o terminal na pasta do projeto e execute `python -m studytrack`.
2. Registre uma sessão fictícia, por exemplo: disciplina `Python`, data de hoje, duração `45` minutos e conteúdo `testes automatizados`.
3. Registre mais uma sessão em outra disciplina.
4. Use a opção de listar sessões e, depois, a opção de relatório para mostrar o tempo total e a divisão por disciplina.
5. Mostre que o programa salva os dados em JSON e que eles continuam disponíveis quando o programa é reiniciado.

Para usar um arquivo de dados dentro da pasta do projeto em PowerShell, antes de iniciar execute:

```powershell
$env:STUDYTRACK_DATA = "$PWD\sessions.json"
python -m studytrack
```

## Roteiro de fala (cerca de 1 minuto)

> O StudyTrack é uma aplicação de linha de comando que ajuda a registrar sessões de estudo e acompanhar o tempo dedicado a cada disciplina. Escolhi esse problema porque é simples, cotidiano e permite demonstrar regras de negócio reais, validação e persistência de dados. O projeto separa o modelo de sessão, o armazenamento JSON, os cálculos de relatório e a interface de terminal. Escrevi testes automatizados com Pytest e configurei uma pipeline de integração contínua no GitHub Actions para executar os testes e verificar a qualidade do código a cada push e Pull Request. O versionamento segue Gitflow: `main` mantém a versão estável, `develop` integra mudanças e branches `feature`, `release` e `hotfix` isolam tipos diferentes de trabalho.

## O que mostrar no GitHub

- A página **Actions** com o workflow executado e o resultado dos checks.
- A pasta `tests/` e o resultado de `pytest -v`.
- O arquivo `.github/workflows/ci.yml`.
- As branches `main`, `develop` e a branch de feature usada na demonstração.
- O Pull Request de feature para `develop`.

## Perguntas que você deve saber responder

**Por que guardar em JSON?** Para manter o MVP simples e evitar configurar um servidor de banco de dados. Em uma versão futura, seria possível migrar para SQLite ou PostgreSQL.

**O que é integração contínua?** É automatizar verificações a cada alteração para identificar problemas cedo, antes de integrar ou entregar o código.

**Qual a função do Pytest?** Executar testes que verificam validações, persistência e cálculos sem precisar conferir tudo manualmente.

**Qual a diferença entre `main` e `develop`?** `main` representa a versão estável; `develop` reúne o trabalho que está sendo preparado para uma próxima versão.

**Para que serve uma branch `feature`?** Desenvolver uma funcionalidade isoladamente e integrá-la por Pull Request após revisão e verificações.

**Para que servem `release` e `hotfix`?** `release` prepara uma versão para entrega; `hotfix` corrige um problema urgente da versão estável.

**O que a pipeline verifica?** Instala o projeto e ferramentas, executa `ruff check .` e roda `pytest -v`. Um check verde indica que essas etapas terminaram sem falhas.
