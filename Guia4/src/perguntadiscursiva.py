from typing import List, Tuple, Dict
from .pergunta import Pergunta

class PerguntaDiscursiva(Pergunta):
    def __init__(self, texto, resposta_esperada=None, case_sensitive=True):
        super().__init__(texto)
        self.resposta_esperada = resposta_esperada
        self.case_sensitive = case_sensitive

    def validar_resposta(self, res):
        if res == self.resposta_esperada:
            return True
        else:
            return False

    def get_tipo(self):
        return "discursiva"