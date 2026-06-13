from typing import List, Tuple, Dict
from .resposta import Resposta

class RespostaObjetiva(Resposta):
    def __init__(self, pergunta, indice_escolhido):
        super().__init__(pergunta)
        self.indice_escolhido = indice_escolhido

    @property
    def esta_correta(self):
        return self.pergunta.validar_resposta(self.indice_escolhido)

    def calcular_pontuacao(self):
        return 1.0 if self.esta_correta else 0.0