from typing import List, Tuple, Dict

class Alternativa:
    def __init__(self, texto, correta, explicacao = None):
        self.texto = texto
        self.correta = correta
        self.explicacao = explicacao

    def get_correta(self):
        return self.correta