from datetime import datetime
from .respostaobjetiva import RespostaObjetiva
from .respostadiscursiva import RespostaDiscursiva
from .perguntamultiplaescolha import PerguntaMultiplaEscolha
from .perguntadiscursiva import PerguntaDiscursiva

class TentativaQuestionario:
    def __init__(self, questionario, usuario):
        self.questionario = questionario
        self.usuario = usuario
        self.data_inicio = datetime.now()
        self.data_fim = None
        self.respostas = []

    def registrar_resposta(self, indice_pergunta, valor):
        pergunta = self.questionario.perguntas[indice_pergunta]
        if isinstance(pergunta, PerguntaMultiplaEscolha):
            resposta = RespostaObjetiva(pergunta, valor)
        else:
            resposta = RespostaDiscursiva(pergunta, valor)
        self.respostas.append(resposta)

    def calcular_pontuacao(self):
        return sum(r.calcular_pontuacao() for r in self.respostas)

    def finalizar(self):
        self.data_fim = datetime.now()
        pontuacao = self.calcular_pontuacao()
        feedback = f"Pontuação final: {pontuacao}"
        return pontuacao, feedback

    def is_finalizado(self):
        return self.data_fim is not None