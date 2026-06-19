import hashlib
from .pessoa import Pessoa


class Professor(Pessoa):

    def __init__(self, nome: str, cpf: str, especialidade: str, senha: str):
        super().__init__(nome, cpf)
        if not especialidade or not especialidade.strip():
            raise ValueError("Especialidade não pode ser vazia.")
        if not senha or len(senha) < 4:
            raise ValueError("Senha deve ter ao menos 4 caracteres.")
        self._especialidade: str = especialidade.strip()
        self._disciplinas_ministradas: list[str] = []
        self._senha_hash: str = hashlib.sha256(senha.encode()).hexdigest()

    @property
    def especialidade(self) -> str:
        return self._especialidade

    @especialidade.setter
    def especialidade(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("Especialidade não pode ser vazia.")
        self._especialidade = valor.strip()

    @property
    def disciplinas_ministradas(self) -> list[str]:
        return list(self._disciplinas_ministradas)

    def autenticar(self, senha: str) -> bool:
        return hashlib.sha256(senha.encode()).hexdigest() == self._senha_hash

    def adicionar_disciplina(self, nome_disciplina: str) -> None:
        nome = nome_disciplina.strip()
        if nome not in self._disciplinas_ministradas:
            self._disciplinas_ministradas.append(nome)

    def remover_disciplina(self, nome_disciplina: str) -> None:
        nome = nome_disciplina.strip()
        if nome in self._disciplinas_ministradas:
            self._disciplinas_ministradas.remove(nome)
        else:
            raise ValueError(f"Disciplina '{nome}' não encontrada para este professor.")

    def apresentar(self) -> str:
        return f"Prof. {self._nome} | Especialidade: {self._especialidade}"

    def __repr__(self) -> str:
        return f"Professor(nome={self._nome!r}, especialidade={self._especialidade!r})"
