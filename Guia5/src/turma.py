from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .aluno import Aluno
    from .disciplina import Disciplina


class Turma:

    def __init__(self, codigo: str, serie: str, capacidade: int = 40):
        if not codigo or not codigo.strip():
            raise ValueError("Código da turma não pode ser vazio.")
        if capacidade <= 0:
            raise ValueError("Capacidade deve ser positiva.")
        self._codigo: str = codigo.strip()
        self._serie: str = serie.strip()
        self._capacidade: int = capacidade
        self._alunos: list[Aluno] = []
        self._disciplinas: list[Disciplina] = []

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def serie(self) -> str:
        return self._serie

    @property
    def capacidade(self) -> int:
        return self._capacidade

    @property
    def alunos(self) -> list[Aluno]:
        return list(self._alunos)

    @property
    def disciplinas(self) -> list[Disciplina]:
        return list(self._disciplinas)

    @property
    def vagas_disponiveis(self) -> int:
        return self._capacidade - len(self._alunos)

    def matricular_aluno(self, aluno: "Aluno") -> None:
        if self.vagas_disponiveis == 0:
            raise OverflowError(f"Turma '{self._codigo}' está cheia.")
        if aluno in self._alunos:
            raise ValueError(f"Aluno '{aluno.nome}' já está matriculado nesta turma.")
        self._alunos.append(aluno)

    def remover_aluno(self, aluno: "Aluno") -> None:
        if aluno not in self._alunos:
            raise ValueError(f"Aluno '{aluno.nome}' não encontrado na turma.")
        self._alunos.remove(aluno)

    def adicionar_disciplina(self, disciplina: "Disciplina") -> None:
        if disciplina in self._disciplinas:
            raise ValueError(f"Disciplina '{disciplina.nome}' já está na turma.")
        self._disciplinas.append(disciplina)

    def gerar_boletim(self, aluno: "Aluno") -> dict[str, dict]:
        if aluno not in self._alunos:
            raise ValueError(f"Aluno '{aluno.nome}' não está matriculado nesta turma.")

        boletim = {}
        for disciplina in self._disciplinas:
            nome_disc = disciplina.nome
            notas = aluno.notas.get(nome_disc, [])
            if notas:
                media = round(sum(notas) / len(notas), 2)
                situacao = "Aprovado" if media >= 6.0 else "Reprovado"
            else:
                media = None
                situacao = "Sem notas"
            boletim[nome_disc] = {
                "notas": notas,
                "media": media,
                "situacao": situacao,
            }
        return boletim

    def gerar_boletim_turma(self) -> dict[str, dict[str, dict]]:
        return {aluno.nome: self.gerar_boletim(aluno) for aluno in self._alunos}

    def total_alunos(self) -> int:
        return len(self._alunos)

    def __str__(self) -> str:
        return (
            f"Turma {self._codigo} | {self._serie} | "
            f"{len(self._alunos)}/{self._capacidade} alunos"
        )

    def __repr__(self) -> str:
        return f"Turma(codigo={self._codigo!r}, serie={self._serie!r}, capacidade={self._capacidade})"
