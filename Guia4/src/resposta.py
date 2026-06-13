from typing import List, Tuple, Dict
from abc import ABC, abstractmethod

class Resposta(ABC):
    def __init__(self, pergunta):
        self.pergunta = pergunta

    @property
    @abstractmethod
    def esta_correta(self):
        pass

    @abstractmethod
    def calcular_pontuacao(self):
        pass