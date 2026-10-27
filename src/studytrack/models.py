"""Modelos e validações do StudyTrack."""

from dataclasses import asdict, dataclass
from datetime import date
from typing import Any


@dataclass(frozen=True)
class StudySession:
    """Representa uma sessão de estudo registrada pelo usuário."""

    subject: str
    date: str
    duration_minutes: int
    notes: str = ""

    def __post_init__(self) -> None:
        if not self.subject.strip():
            raise ValueError("A disciplina não pode ficar vazia.")
        try:
            parsed_date = date.fromisoformat(self.date)
            if parsed_date.isoformat() != self.date:
                raise ValueError("formato diferente de AAAA-MM-DD")
        except ValueError as exc:
            raise ValueError("A data deve estar no formato AAAA-MM-DD.") from exc
        if self.duration_minutes <= 0:
            raise ValueError("A duração deve ser maior que zero.")

    def to_dict(self) -> dict[str, Any]:
        """Converte a sessão para um dicionário serializável em JSON."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "StudySession":
        """Cria uma sessão a partir de um dicionário."""
        return cls(
            subject=str(data["subject"]),
            date=str(data["date"]),
            duration_minutes=int(data["duration_minutes"]),
            notes=str(data.get("notes", "")),
        )
