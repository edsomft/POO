from typing import List, Tuple, Dict
from src.tentativaquestionario import TentativaQuestionario

class Questionario:
    def __init__(self, titulo):
        self.titulo = titulo
        self.perguntas = []
    
    def adicionar_pergunta(self, pergunta):
        self.perguntas.append(pergunta)
    
    def criar_attempt(self, usuario):
        return TentativaQuestionario(self, usuario)
        
