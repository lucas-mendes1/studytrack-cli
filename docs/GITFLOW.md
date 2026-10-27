# Roteiro Gitflow para o StudyTrack

> Execute os comandos em um terminal dentro da pasta do projeto. Substitua `SEU-USUARIO` pela sua conta do GitHub.

## Preparar o repositório

Crie no GitHub um repositório público chamado `studytrack-cli` (sem README inicial, pois este projeto já tem um).

```bash
git init -b main
git add .
git commit -m "chore: cria estrutura inicial do StudyTrack"
git remote add origin https://github.com/SEU-USUARIO/studytrack-cli.git
git push -u origin main

git switch -c develop
git push -u origin develop
```

## Simular uma feature e o Pull Request

Escolha uma melhoria pequena e real para implementar. Exemplo: acrescentar uma seção no README mostrando uma sessão fictícia e a saída de um relatório.

```bash
git switch develop
git pull
git switch -c feature/exemplo-de-relatorio
# Edite README.md e salve a alteração.
git add README.md
git commit -m "docs: adiciona exemplo de relatorio de estudos"
git push -u origin feature/exemplo-de-relatorio
```

No GitHub, abra um Pull Request de `feature/exemplo-de-relatorio` para `develop`. Confira se o check da pipeline passou e faça o merge. Depois atualize a branch local:

```bash
git switch develop
git pull
```

## Preparar uma release

```bash
git switch -c release/1.0.0 develop
# Revise README.md e CHANGELOG.md; rode pytest -v e ruff check .
git add README.md CHANGELOG.md
git commit -m "chore: prepara release 1.0.0"
git switch main
git merge --no-ff release/1.0.0 -m "release: versão 1.0.0"
git tag -a v1.0.0 -m "StudyTrack 1.0.0"
git push origin main --tags
git switch develop
git merge --no-ff release/1.0.0 -m "chore: sincroniza release 1.0.0"
git push origin develop
git branch -d release/1.0.0
```

**Observação:** o merge local com `--no-ff` registra a integração no histórico. Se a turma exige que todo merge seja feito por Pull Request, adapte o roteiro ao processo solicitado pelo professor.

## Demonstrar um hotfix

Para demonstrar o fluxo sem inventar uma falha no código, faça uma correção real de documentação ou validação, partindo da versão estável:

```bash
git switch main
git switch -c hotfix/mensagem-validacao
# Faça uma pequena correção real no código ou na documentação.
git add .
git commit -m "fix: melhora mensagem de validacao"
git push -u origin hotfix/mensagem-validacao
```

Depois, abra um Pull Request para `main`, aguarde a pipeline e faça o merge. Integre a mesma correção em `develop` (por Pull Request ou merge, conforme o procedimento da turma) e remova a branch de hotfix após concluir.

**Importante:** não execute release/hotfix só por executar. Explique o motivo, a branch de origem, o destino e o que a pipeline verificou.
