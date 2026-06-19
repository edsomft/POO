from abc import ABC, abstractmethod


class Pessoa(ABC):

    def __init__(self, nome: str, cpf: str):
        if not nome or not nome.strip():
            raise ValueError("Nome não pode ser vazio.")
        if not cpf or not cpf.strip():
            raise ValueError("CPF não pode ser vazio.")
        self._nome = nome.strip()
        self._cpf = cpf.strip()

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("Nome não pode ser vazio.")
        self._nome = valor.strip()

    @property
    def cpf(self) -> str:
        return self._cpf

    @abstractmethod
    def apresentar(self) -> str:
        """Retorna uma apresentação textual da pessoa."""

    def __str__(self) -> str:
        return self.apresentar()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(nome={self._nome!r}, cpf={self._cpf!r})"
