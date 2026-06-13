from typing import List, Tuple, Dict
from .pergunta import Pergunta

class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, texto, alternativas, explicacao_geral=None):
        super().__init__(texto, explicacao_geral)
        self.alternativas = alternativas

    def validar_resposta(self, indice):
        resposta = self.alternativas[indice]
        return resposta.get_correta()
    
    def get_alternativa_correta(self):
        for res in self.alternativas:
            if res.get_correta() == True:
                return res
    
    def get_tipo(self):
        return "multipla_escolha"
    
    def get_explicacao(self):
        return self.explicacao_geral
    