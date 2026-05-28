from typing import List, Tuple, Dict

class PerguntaMultiplaEscolha():
    def __init__(self, texto, alternativas, explicacao_geral = None):
        self.texto = texto
        self.alternativas = alternativas
        self.explicacao_geral = explicacao_geral

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
    