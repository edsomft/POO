from typing import List, Tuple, Dict
from abc import ABC, abstractmethod

class Pergunta(ABC):
    def __init__(self, texto, explicacao_geral=None):
        self.texto = texto
        self.explicacao_geral = explicacao_geral

    @abstractmethod
    def validar_resposta(self, resposta):
        pass

    def get_explicacao(self):
        return self.explicacao_geral

    @abstractmethod
    def get_tipo(self):
        pass