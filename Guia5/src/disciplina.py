from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .professor import Professor


class Disciplina:

    def __init__(self, nome: str, carga_horaria: int, professor: "Professor"):
        if not nome or not nome.strip():
            raise ValueError("Nome da disciplina não pode ser vazio.")
        if carga_horaria <= 0:
            raise ValueError("Carga horária deve ser positiva.")
        self._nome: str = nome.strip()
        self._carga_horaria: int = carga_horaria
        self._professor: Professor = professor
        professor.adicionar_disciplina(self._nome)

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def carga_horaria(self) -> int:
        return self._carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, valor: int) -> None:
        if valor <= 0:
            raise ValueError("Carga horária deve ser positiva.")
        self._carga_horaria = valor

    @property
    def professor(self) -> "Professor":
        return self._professor

    @professor.setter
    def professor(self, novo: "Professor") -> None:
        self._professor.remover_disciplina(self._nome)
        self._professor = novo
        novo.adicionar_disciplina(self._nome)

    def __str__(self) -> str:
        return f"Disciplina: {self._nome} ({self._carga_horaria}h) | Prof. {self._professor.nome}"

    def __repr__(self) -> str:
        return f"Disciplina(nome={self._nome!r}, carga_horaria={self._carga_horaria})"
