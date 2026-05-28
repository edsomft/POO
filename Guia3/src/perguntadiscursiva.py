from typing import List, Tuple, Dict

class PerguntaDiscursiva:
    def __init__(self, texto, resposta_esperada = None):
        self.texto = texto
        self.resposta_esperada = resposta_esperada

    def validar_resposta(self, res):
        if res == self.resposta_esperada:
            return True
        else:
            return False

    def get_tipo(self):
        return "discursiva"