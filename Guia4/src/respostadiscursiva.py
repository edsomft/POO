from typing import List, Tuple, Dict
from .resposta import Resposta

class RespostaDiscursiva(Resposta):
    def __init__(self, pergunta, texto_resposta):
        super().__init__(pergunta)
        self.texto_resposta = texto_resposta

    @property
    def esta_correta(self):
        return self.pergunta.validar_resposta(self.texto_resposta)

    def calcular_pontuacao(self):
        return 1.0 if self.esta_correta else 0.0