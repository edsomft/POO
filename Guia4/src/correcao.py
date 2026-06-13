from typing import List, Tuple, Dict
from .llmservice import LLMService


class Correcao:
    @staticmethod
    def criar_prompt_correcao(pergunta, resposta_aluno):
        service = LLMService()
        return service._criar_prompt(pergunta, resposta_aluno)

    @staticmethod
    def corrigir_discursiva(pergunta, resposta_aluno, service=None):
        if service is None:
            service = LLMService()

        return service.corrigir_resposta(pergunta, resposta_aluno)