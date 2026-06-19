from .pessoa import Pessoa


class Aluno(Pessoa):
    _contador_matricula: int = 1000  # atributo de classe

    def __init__(self, nome: str, cpf: str):
        super().__init__(nome, cpf)
        Aluno._contador_matricula += 1
        self._matricula: int = Aluno._contador_matricula
        self._notas: dict[str, list[float]] = {}   # disciplina_nome → [notas]

    @property
    def matricula(self) -> int:
        return self._matricula

    @property
    def notas(self) -> dict[str, list[float]]:
        return {k: list(v) for k, v in self._notas.items()}

    def adicionar_nota(self, disciplina: str, nota: float) -> None:
        if not (0.0 <= nota <= 10.0):
            raise ValueError(f"Nota deve estar entre 0 e 10. Recebido: {nota}")
        self._notas.setdefault(disciplina, []).append(nota)

    def media(self, disciplina: str) -> float:
        notas = self._notas.get(disciplina)
        if not notas:
            raise ValueError(f"Nenhuma nota registrada para '{disciplina}'.")
        return sum(notas) / len(notas)

    def aprovado(self, disciplina: str, minimo: float = 6.0) -> bool:
        return self.media(disciplina) >= minimo

    @classmethod
    def resetar_contador(cls, valor: int = 1000) -> None:
        cls._contador_matricula = valor

    def apresentar(self) -> str:
        return f"Aluno: {self._nome} | Matrícula: {self._matricula}"

    def __repr__(self) -> str:
        return f"Aluno(nome={self._nome!r}, matricula={self._matricula})"
