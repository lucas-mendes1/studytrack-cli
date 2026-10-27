"""Persistência local das sessões em arquivo JSON."""

import json
from pathlib import Path

from studytrack.models import StudySession


def load_sessions(path: Path) -> list[StudySession]:
    """Carrega as sessões; retorna uma lista vazia se o arquivo não existir."""
    if not path.exists():
        return []

    try:
        raw_data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"O arquivo de dados não contém JSON válido: {path}") from exc

    if not isinstance(raw_data, list):
        raise TypeError("O arquivo de dados deve conter uma lista de sessões.")

    try:
        return [StudySession.from_dict(item) for item in raw_data]
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError("Há uma sessão inválida no arquivo de dados.") from exc


def save_sessions(path: Path, sessions: list[StudySession]) -> None:
    """Salva todas as sessões em JSON, criando a pasta se necessário."""
    path.parent.mkdir(parents=True, exist_ok=True)
    content = [session.to_dict() for session in sessions]
    path.write_text(
        json.dumps(content, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
