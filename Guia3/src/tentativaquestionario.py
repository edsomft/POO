from typing import List, Tuple, Dict

class TentativaQuestionario:
    def __init__(self, questionario, usuario):
        self.questionario = questionario
        self.usuario = usuario
        self.respostas = []
    
    def registrar_resposta(self, indice, resposta):
        registro = [indice, resposta]
        self.respostas.append(registro)

    def calcular_pontuacao(self):
        pontuacao = 0
        for res in self.respostas:
            pergunta = self.questionario.perguntas[res[0]]

            if pergunta.validar_resposta(res[1]) == True:
                pontuacao = pontuacao +1
        return pontuacao
    
    def finalizar(self):
        self._finalizado = True
        pontuacao = self.calcular_pontuacao()
        total = len(self.questionario.perguntas)
        feedback = f"Você acertou {pontuacao} de {total} questões."
        return pontuacao, feedback

    def is_finalizado(self):
        return self._finalizado
            